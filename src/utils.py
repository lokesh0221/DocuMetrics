"""
Utility functions for the documentation analyzer.
"""

import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import os

def load_prompt_template(prompt_type: str) -> List[tuple[str, str]]:
    """Load prompt template from JSON file."""
    prompt_file = os.path.join(os.path.dirname(__file__), '..', 'prompts', f'{prompt_type}.json')
    with open(prompt_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [(msg['role'], msg['content']) for msg in data['messages']]

def save_results(url: str, analysis: Dict[str, Any], revised_content: Optional[str] = None):
    """Save analysis results and revised content to files."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save analysis as JSON
    result_data = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "analysis": analysis
    }
    
    json_file = os.path.join(output_dir, f"analysis_{timestamp}.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, indent=2, ensure_ascii=False)
    
    # Save revised content if available
    if revised_content:
        content_file = os.path.join(output_dir, f"revised_content_{timestamp}.txt")
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(revised_content)

def print_results(url: str, analysis: Dict[str, Any], revised_content: Optional[str] = None):
    """Print analysis results in a readable format."""
    print("\n" + "="*60)
    print("DOCUMENTATION ANALYSIS RESULTS")
    print("="*60)
    
    print(f"\nURL: {url}")
    print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    categories = ['readability', 'structure', 'completeness', 'style_guidelines']
    
    for category in categories:
        if category in analysis:
            data = analysis[category]
            print(f"\n{'-'*30}")
            print(f"{category.upper().replace('_', ' ')}")
            print(f"{'-'*30}")
            print(f"Score: {data.get('score', 'N/A')}")
            
            if data.get('issues'):
                print("\nIssues:")
                for i, issue in enumerate(data['issues'], 1):
                    print(f"  {i}. {issue}")
            
            if data.get('suggestions'):
                print("\nSuggestions:")
                for i, suggestion in enumerate(data['suggestions'], 1):
                    print(f"  {i}. {suggestion}")
    
    if revised_content:
        print(f"\n{'='*60}")
        print("REVISED CONTENT")
        print("="*60)
        print(revised_content) 