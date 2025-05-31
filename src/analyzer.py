"""
LangChain-Powered Documentation Analyzer
Main analyzer class implementation.
"""

import os
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from src.models import DocumentationAnalysis
from src.utils import load_prompt_template

class DocumentationAnalyzer:
    """Main class for analyzing documentation using LangChain."""
    
    def __init__(self, api_key: str):
        """Initialize the analyzer with LangChain components."""
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=api_key,
        )
        
        # Initialize parsers
        self.json_parser = JsonOutputParser(pydantic_object=DocumentationAnalysis)
        self.str_parser = StrOutputParser()
        
        # Load prompt templates
        self.analysis_prompt = ChatPromptTemplate.from_messages(load_prompt_template("analysis"))
        self.revision_prompt = ChatPromptTemplate.from_messages(load_prompt_template("revision"))
        
        # Create chains
        self.analysis_chain = self.analysis_prompt | self.llm | self.json_parser
        self.revision_chain = self.revision_prompt | self.llm | self.str_parser

    def scrape_page(self, url: str) -> str:
        """Scrape content from a documentation page."""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            print(f"Scraping content from: {url}")
            driver.get(url)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            time.sleep(15)
            
            content_parts = []
            main_selectors = [
                "main", ".main-content", "#main-content", 
                ".article-content", ".content", ".post-content",
                ".entry-content", "[role='main']"
            ]
            
            # Try multiple content extraction strategies
            for selector in main_selectors:
                try:
                    main_element = driver.find_element(By.CSS_SELECTOR, selector)
                    if main_element and main_element.text.strip():
                        elements = main_element.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6, p, ul, ol, li, pre, code, div")
                        for element in elements:
                            text = element.text.strip()
                            if text and len(text) > 10:
                                tag = element.tag_name.lower()
                                if tag.startswith('h') and len(tag) == 2:
                                    content_parts.append(f"\n{'#' * int(tag[1])} {text}\n")
                                else:
                                    content_parts.append(text)
                        break
                except Exception:
                    continue
            
            if not content_parts:
                content_text = driver.execute_script("""
                    var scripts = document.querySelectorAll('script, style, nav, footer, header, .nav, .footer, .header');
                    scripts.forEach(function(el) { el.remove(); });
                    var mainContent = document.querySelector('main, .main-content, #main-content, .article-content, .content') || document.body;
                    return mainContent.innerText || mainContent.textContent || '';
                """)
                if content_text:
                    content_parts = [content_text.strip()]
            
            if content_parts:
                content = "\n\n".join(content_parts)
                lines = [line.strip() for line in content.split('\n') if line.strip() and len(line.strip()) > 3]
                return "\n".join(lines)
            
            raise Exception("No substantial content found")
            
        except Exception as e:
            print(f"Error scraping page: {e}")
            raise
        finally:
            driver.quit()

    def analyze_content(self, content: str, url: str) -> Dict[str, Any]:
        """Analyze content using LangChain."""
        try:
            print("Analyzing content with LangChain + Gemini...")
            format_instructions = self.json_parser.get_format_instructions()
            result = self.analysis_chain.invoke({
                "content": content,
                "url": url,
                "format_instructions": format_instructions
            })
            return result.dict() if hasattr(result, 'dict') else result
        except Exception as e:
            print(f"Error during analysis: {e}")
            return {cat: {
                "score": "Fair",
                "issues": ["Analysis failed"],
                "suggestions": ["Please try again"]
            } for cat in ["readability", "structure", "completeness", "style_guidelines"]}

    def revise_content(self, original_content: str, analysis: Dict[str, Any]) -> str:
        """Revise content based on analysis."""
        try:
            print("Generating revised content...")
            feedback_parts = []
            for category, data in analysis.items():
                feedback_parts.extend([
                    f"\n{category.title().replace('_', ' ')} Analysis:",
                    f"Score: {data.get('score', 'N/A')}",
                    "Issues:" if data.get('issues') else "",
                    *[f"- {issue}" for issue in data.get('issues', [])],
                    "Suggestions:" if data.get('suggestions') else "",
                    *[f"- {suggestion}" for suggestion in data.get('suggestions', [])]
                ])
            
            return self.revision_chain.invoke({
                "original_content": original_content,
                "feedback": "\n".join(feedback_parts)
            })
        except Exception as e:
            print(f"Error during revision: {e}")
            raise

    def calculate_overall_score(self, analysis: Dict[str, Any]) -> str:
        """Calculate overall score."""
        scores = []
        score_values = {'Excellent': 4, 'Good': 3, 'Fair': 2, 'Poor': 1}
        
        for category_data in analysis.values():
            score = category_data.get('score', 'Fair')
            if score in score_values:
                scores.append(score_values[score])
        
        if not scores:
            return "Unknown"
        
        avg = sum(scores) / len(scores)
        if avg >= 3.5:
            return "Excellent"
        elif avg >= 2.5:
            return "Good"
        elif avg >= 1.5:
            return "Fair"
        else:
            return "Poor"

    def analyze_documentation(self, url: str) -> Dict[str, Any]:
        """Main method to analyze documentation."""
        content = self.scrape_page(url)
        analysis = self.analyze_content(content, url)
        return analysis

    def generate_revision(self, url: str, analysis: Dict[str, Any]) -> str:
        """Generate revised content based on analysis."""
        content = self.scrape_page(url)
        return self.revise_content(content, analysis) 