# app/nodes/research.py
from app.state_definitions import AppState
from models.prompts.research_prompts import RESEARCH_PROMPT
from langchain.llms import OpenAI

def research_node(state: AppState) -> dict:
    """Research node that gathers information."""
    llm = OpenAI()
    research_result = llm.invoke(RESEARCH_PROMPT.format(
        task=state["task"],
        context=state["context"]
    ))
    
    return {"context": research_result}
