# setup.py
from setuptools import setup, find_packages

setup(
    name="langgraph_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langgraph>=0.0.10",
        "langchain>=0.0.267",
        "langchain-openai>=0.0.2",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A LangGraph-based application",
    keywords="langgraph, langchain, llm",
    python_requires=">=3.9",
)
