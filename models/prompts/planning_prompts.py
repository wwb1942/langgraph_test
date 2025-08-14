# models/prompts/planning_prompts.py
from langchain.prompts import PromptTemplate

PLANNING_PROMPT = PromptTemplate(
    template="""
    Based on the following task and research context, create a step-by-step plan for completion.
    
    TASK: {task}
    
    RESEARCH CONTEXT: {context}
    
    Provide a numbered list of steps to complete the task:
    """,
    input_variables=["task", "context"]
)
