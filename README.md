# LangChain Documentation Analyzer

A powerful documentation analysis tool powered by LangChain and Google's Gemini AI. This tool helps improve documentation by analyzing readability, structure, completeness, and adherence to style guidelines.

## Features

- **Content Scraping**: Automatically extracts content from documentation pages
- **Comprehensive Analysis**: Evaluates multiple aspects of documentation:
  - Readability for non-technical users
  - Document structure and organization
  - Content completeness
  - Style guideline adherence
- **AI-Powered Improvements**: Generates revised versions with enhanced clarity
- **Structured Output**: Provides analysis results in both JSON and human-readable formats
- **Markdown Support**: Handles and generates Markdown-formatted content
- **Interactive Web Interface**: User-friendly Streamlit interface with visualizations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lokesh0221/DocuMetrics
cd documentation-analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Set up environment variables:
Create a `.env` file in the project root with:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Web Interface

You can run the Streamlit app in two ways:

1. Using the run script (recommended):
```bash
python run_streamlit.py
```

2. Or directly with Streamlit:
```bash
streamlit run src/streamlit_app.py
```

This will open a web interface where you can:
1. Enter a documentation URL
2. View analysis results with interactive visualizations
3. Download analysis results and revised content
4. Explore detailed feedback in an organized interface

### Command Line

1. Analyze a documentation page:
```bash
python -m src.main https://your-documentation-url
```

2. Or run interactively:
```bash
python -m src.main
```

The tool will:
1. Scrape the content from the provided URL
2. Analyze the documentation using LangChain + Gemini
3. Generate improvement suggestions
4. Create a revised version
5. Save results to the `output` directory

## Output

The tool generates two types of output files in the `output` directory:
- `analysis_TIMESTAMP.json`: Detailed analysis results in JSON format
- `revised_content_TIMESTAMP.md`: Improved version of the documentation in Markdown

## Project Structure

```
documentation-analyzer/
├── src/
│   ├── __init__.py
│   ├── main.py           # Command-line interface
│   ├── streamlit_app.py  # Web interface
│   ├── analyzer.py       # Main analyzer class
│   ├── models.py         # Pydantic models
│   └── utils.py          # Utility functions
├── prompts/
│   ├── analysis.json     # Analysis prompt template
│   └── revision.json     # Revision prompt template
├── output/               # Generated results
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Requirements

- Python 3.8+
- Google Gemini API key
- Chrome/Chromium browser (for Selenium)
- Streamlit for web interface

## Features of the Web Interface

1. **Interactive Analysis**
   - Simple URL input
   - Real-time analysis progress
   - Visual feedback

2. **Results Display**
   - Color-coded overall score
   - Tabbed interface for detailed analysis

3. **Download Options**
   - JSON analysis results
   - Markdown revised content
   - Easy export functionality

4. **User-Friendly Design**
   - Clean, modern interface
   - Intuitive navigation
   - Responsive layout

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
