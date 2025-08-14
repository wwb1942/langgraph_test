# app/graphs/main_graph.py
# app/graphs/main_graph.py (extended)
from langgraph.graph import StateGraph
from app.state_definitions import AppState
from app.nodes.research import research_node
from app.nodes.planning import planning_node
from app.nodes.execution import execution_node
from app.nodes.router import router_node

def create_main_graph():
    """Create the main application graph with conditional branching."""
    graph = StateGraph(AppState)
    
    # Add nodes
    graph.add_node("research", research_node)
    graph.add_node("plan", planning_node)
    graph.add_node("execute", execution_node)
    graph.add_node("router", router_node)
    
    # Add error handler node
    def error_handler(state):
        return {"messages": state["messages"] + [{"role": "system", "content": f"Error: {state['error']}"}]}
    
    graph.add_node("error_handler", error_handler)
    
    # Add finish node
    def finish(state):
        return {"messages": state["messages"] + [{"role": "system", "content": "Task completed successfully."}]}
    
    graph.add_node("finish", finish)
    
    # Connect with conditional edges
    graph.add_edge("research", "router")
    graph.add_edge("plan", "router")
    graph.add_edge("execute", "router")
    
    # Add conditional edges from router
    graph.add_conditional_edges(
        "router",
        {
            "error_handler": lambda state: state.get("error") is not None,
            "research": lambda state: not state.get("context"),
            "plan": lambda state: state.get("context") and not state.get("plan"),
            "execute": lambda state: state.get("plan") and state["status"] != "execution_complete",
            "finish": lambda state: state["status"] == "execution_complete"
        }
    )
    
    # Set entry point
    graph.set_entry_point("router")
    
    return graph.compile()

