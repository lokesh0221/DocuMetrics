#!/usr/bin/env python3
"""
LangChain-Powered Documentation Improvement Agent
Analyzes documentation and suggests improvements using LangChain.
"""

import os
import sys
from dotenv import load_dotenv
from .analyzer import DocumentationAnalyzer
from .utils import print_results, save_results

def main():
    """Main function to run the documentation analyzer."""
    try:
        # Load environment variables
        load_dotenv()
        
        # Check API key
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print("Error: Google Gemini API key not found! Set GEMINI_API_KEY environment variable.")
            sys.exit(1)
        
        # Get URL from command line or user input
        if len(sys.argv) < 2:
            url = input("Enter the documentation URL to analyze: ").strip()
            if not url:
                print("No URL provided. Exiting.")
                sys.exit(1)
        else:
            url = sys.argv[1]
        
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            print("Please provide a valid URL starting with http:// or https://")
            sys.exit(1)
        
        print("Starting LangChain-powered documentation analysis...")
        print("This may take a few minutes...\n")
        
        # Initialize and run analyzer
        analyzer = DocumentationAnalyzer(api_key)
        analysis, revised_content = analyzer.analyze_documentation(url)
        
        # Display and save results
        print_results(url, analysis, revised_content)
        save_results(url, analysis, revised_content)
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 