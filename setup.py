from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="documetrics",
    version="0.1.0",
    author="Lokesh",
    author_email="lokesh0221@github.com",
    description="AI-powered documentation analysis and improvement tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lokesh0221/DocuMetrics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.32.0",
        "langchain>=0.1.12",
        "python-dotenv",
        "google-generativeai",
        "requests",
        "beautifulsoup4",
        "markdown",
    ],
    entry_points={
        "console_scripts": [
            "documetrics=src.main:main",
        ],
    },
) 