# app/nodes/planning.py
from app.state_definitions import AppState
from models.prompts.planning_prompts import PLANNING_PROMPT
from langchain.llms import ChatOpenAI

def planning_node(state: AppState) -> dict:
    """Planning node that creates a plan based on research."""
    llm = ChatOpenAI(model="gpt-4")
    
    # Generate plan based on context and task
    planning_result = llm.invoke(PLANNING_PROMPT.format(
        task=state["task"],
        context=state["context"]
    ))
    
    # Parse plan into steps
    plan_steps = planning_result.content.split("\n")
    plan_steps = [step.strip() for step in plan_steps if step.strip()]
    
    return {
        "plan": plan_steps,
        "status": "planning_complete"
    }
