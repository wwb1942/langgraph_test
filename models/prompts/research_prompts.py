# models/prompts/research_prompts.py
from langchain.prompts import PromptTemplate

RESEARCH_PROMPT = PromptTemplate(
    template="""
    You are a research assistant tasked with gathering information on the following task:
    
    TASK: {task}
    
    EXISTING CONTEXT: {context}
    
    Please gather relevant information to help complete this task. Be thorough but concise.
    """,
    input_variables=["task", "context"]
)
