# app/nodes/execution.py
from app.state_definitions import AppState
from app.tools.data_tools import process_data
from models.prompts.execution_prompts import EXECUTION_PROMPT
from langchain.llms import ChatOpenAI

def execution_node(state: AppState) -> dict:
    """Execution node that performs actions based on the plan."""
    llm = ChatOpenAI(model="gpt-4")
    
    # Execute each step in the plan
    results = {}
    for step_idx, step in enumerate(state["plan"]):
        execution_result = llm.invoke(EXECUTION_PROMPT.format(
            step=step,
            context=state["context"],
            previous_results=results
        ))
        
        # Process any data as needed
        processed_result = process_data(execution_result.content)
        results[f"step_{step_idx+1}"] = processed_result
    
    # Create a message summarizing the execution
    summary_message = {
        "role": "assistant",
        "content": f"Executed {len(state['plan'])} steps with {len(results)} results."
    }
    
    return {
        "results": results,
        "messages": state["messages"] + [summary_message],
        "status": "execution_complete"
    }
