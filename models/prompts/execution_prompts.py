# models/prompts/execution_prompts.py
from langchain.prompts import PromptTemplate

EXECUTION_PROMPT = PromptTemplate(
    template="""
    Execute the following step of the plan:
    
    STEP: {step}
    
    CONTEXT: {context}
    
    PREVIOUS RESULTS: {previous_results}
    
    Please provide the output of executing this step.
    """,
    input_variables=["step", "context", "previous_results"]
)
