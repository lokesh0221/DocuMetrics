"""
Run script for the Streamlit app.
"""

import streamlit.web.cli as stcli
import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

if __name__ == "__main__":
    # Change to the project root directory
    os.chdir(project_root)
    
    sys.argv = ["streamlit", "run", "src/streamlit_app.py"]
    sys.exit(stcli.main()) 