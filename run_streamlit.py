"""
Streamlit Cloud entry point.
"""
import streamlit.web.cli as stcli
import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "src/streamlit_app.py"]
    sys.exit(stcli.main()) 