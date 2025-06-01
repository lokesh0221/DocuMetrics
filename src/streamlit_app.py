"""
Streamlit frontend for the Documentation Analyzer.
"""

import os
import sys
from pathlib import Path

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from dotenv import load_dotenv
from src.analyzer import DocumentationAnalyzer
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Documentation Analyzer",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .score-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        text-align: center;
    }
    .excellent { background-color: #90EE90; }
    .good { background-color: #98FB98; }
    .fair { background-color: #FFB347; }
    .poor { background-color: #FF6961; }
</style>
""", unsafe_allow_html=True)

def display_analysis_results(analysis, url):
    """Display analysis results in a structured format."""
    # Overall score
    analyzer = DocumentationAnalyzer(os.getenv('GEMINI_API_KEY'))
    overall_score = analyzer.calculate_overall_score(analysis)
    score_class = overall_score.lower()
    
    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Analysis Results")
        st.markdown(f"**URL:** {url}")
        st.markdown(f"**Analysis Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Display overall score
        st.markdown(f"""
        <div class="score-box {score_class}">
            <h3>Overall Score: {overall_score}</h3>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # Download buttons
        st.subheader("Download Results")
        
        # Create JSON for download
        json_data = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis
        }
        st.download_button(
            label="Download Analysis (JSON)",
            data=json.dumps(json_data, indent=2),
            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    # Detailed analysis for each category
    st.markdown("## Task 1: Detailed Analysis")
    st.markdown("This section provides a comprehensive analysis of your documentation across multiple dimensions.")
    tabs = st.tabs(['Readability', 'Structure', 'Completeness', 'Style Guidelines'])
    
    for tab, category in zip(tabs, ['readability', 'structure', 'completeness', 'style_guidelines']):
        with tab:
            if category in analysis:
                data = analysis[category]
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Score:** {data['score']}")
                    if data.get('issues'):
                        st.markdown("**Issues:**")
                        for issue in data['issues']:
                            st.markdown(f"- {issue}")
                
                with col2:
                    if data.get('suggestions'):
                        st.markdown("**Suggestions:**")
                        for suggestion in data['suggestions']:
                            st.markdown(f"- {suggestion}")

def main():
    """Main Streamlit application."""
    st.title("📝 Documentation Analyzer")
    st.markdown("""
    Analyze and improve your documentation using AI-powered insights.
    This tool evaluates readability, structure, completeness, and style guidelines.
    """)
    
    # Check for API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        st.error("Error: Google Gemini API key not found! Set GEMINI_API_KEY environment variable.")
        return
    
    # URL input
    url = st.text_input("Enter documentation URL:", placeholder="https://example.com/docs")
    
    # Initialize session state for storing analysis results
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    
    if st.button("Analyze Documentation"):
        if not url:
            st.warning("Please enter a URL to analyze.")
            return
        
        if not url.startswith(('http://', 'https://')):
            st.error("Please provide a valid URL starting with http:// or https://")
            return
        
        try:
            with st.spinner("Analyzing documentation... This may take a few minutes."):
                # Initialize analyzer
                analyzer = DocumentationAnalyzer(api_key)
                
                # Run analysis
                analysis = analyzer.analyze_documentation(url)
                
                # Store analysis results in session state
                st.session_state.analysis_results = analysis
                st.session_state.current_url = url
                
                # Display results
                display_analysis_results(analysis, url)
                
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
    
    # Show revision button only if we have analysis results
    if st.session_state.analysis_results is not None:
        st.markdown("## Task 2: Generate Revised Content (Bonus)")
        st.markdown("Based on the analysis, generate an improved version of your documentation.")
        if st.button("Generate Revised Content"):
            try:
                with st.spinner("Generating revised content... This may take a few minutes."):
                    # Initialize analyzer
                    analyzer = DocumentationAnalyzer(api_key)
                    
                    # Generate revision
                    revised_content = analyzer.generate_revision(st.session_state.current_url, st.session_state.analysis_results)
                    
                    # Show revised content
                    if revised_content:
                        st.subheader("Revised Content")
                        st.markdown(revised_content)
                        
                        # Download revised content
                        st.download_button(
                            label="Download Revised Content (Text)",
                            data=revised_content,
                            file_name=f"revised_content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    
            except Exception as e:
                st.error(f"Error generating revised content: {str(e)}")

if __name__ == "__main__":
    main() 