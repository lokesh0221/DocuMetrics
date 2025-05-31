"""
Streamlit Cloud entry point.
"""
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

if __name__ == "__main__":
    try:
        import streamlit.web.cli as stcli
        from streamlit.web.cli import main

        # Get the absolute path to the Streamlit app
        app_path = os.path.join(project_root, "src", "streamlit_app.py")
        
        # Set up Streamlit command-line arguments
        sys.argv = ["streamlit", "run", app_path, "--server.port=8501"]
        
        # Run Streamlit
        if stcli.main() == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error running Streamlit: {str(e)}")
        sys.exit(1) 