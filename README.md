# DocuMetrics

<div align="center">

![DocuMetrics Logo](https://img.shields.io/badge/DocuMetrics-AI%20Documentation%20Analysis-blue)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.12-green)](https://python.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

</div>

## 🚀 Overview

DocuMetrics is an intelligent documentation analysis platform powered by LangChain and Google's Gemini AI. Transform your documentation quality with advanced metrics and AI-driven insights.

### 🎯 Key Features

- **📊 Comprehensive Analysis**
  - Readability Assessment
  - Structure Evaluation
  - Completeness Check
  - Style Guidelines Compliance

- **🤖 AI-Powered Improvements**
  - Smart Content Recommendations
  - Auto-Generated Revisions
  - Context-Aware Suggestions

- **💻 User-Friendly Interface**
  - Interactive Web Dashboard
  - Real-Time Analysis
  - One-Click Improvements
  - Downloadable Reports

## 🛠️ Installation

1. **Clone the Repository**
```bash
<<<<<<< HEAD
git clone <repository-url>
cd DocuMetrics
=======
git clone https://github.com/lokesh0221/DocuMetrics
cd documentation-analyzer
>>>>>>> 9cade5dfefb5bc591474658c9616b63c2a21cadb
```

2. **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -e .
```

4. **Configure Environment**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Usage

### 🌐 Web Interface

**Option 1: Quick Start**
```bash
python run_streamlit.py
```

**Option 2: Direct Launch**
```bash
streamlit run src/streamlit_app.py
```

### 📊 Features

1. **Documentation Analysis**
   - Enter your documentation URL
   - Get instant quality metrics
   - Review detailed feedback

2. **AI-Powered Improvements**
   - Generate revised content
   - Download improved versions
   - Track quality metrics

3. **Export Options**
   - JSON analysis reports
   - Markdown revised content
   - Detailed recommendations

## 🏗️ Project Structure

```
DocuMetrics/
├── src/
│   ├── __init__.py
│   ├── main.py           # CLI interface
│   ├── streamlit_app.py  # Web interface
│   ├── analyzer.py       # Core analyzer
│   ├── models.py         # Data models
│   └── utils.py          # Utilities
├── prompts/
│   ├── analysis.json     # Analysis templates
│   └── revision.json     # Revision templates
├── output/               # Generated content
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## 🔧 Requirements

- Python 3.8+
- Google Gemini API key
- Chrome/Chromium browser
- Internet connection

## 🤝 Contributing

We welcome contributions! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

<<<<<<< HEAD
- Powered by Google's Gemini AI
- Built with LangChain
- Streamlit for the web interface 
=======
Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
>>>>>>> 9cade5dfefb5bc591474658c9616b63c2a21cadb
