# app/nodes/router.py
from app.state_definitions import AppState

def router_node(state: AppState) -> str:
    """Router node that determines next steps based on current state."""
    if state.get("error"):
        return "error_handler"
    
    if state["status"] == "execution_complete":
        return "finish"
    
    if not state.get("context"):
        return "research"
    elif not state.get("plan"):
        return "plan"
    else:
        return "execute"
