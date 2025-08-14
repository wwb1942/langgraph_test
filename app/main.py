# app/main.py
# app/main.py (complete version)
import os
import sys
from typing import Dict, Any

# Add parent directory to path so we can import from other directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.graphs.main_graph import create_main_graph
from app.state_definitions import AppState
from app.utils.helpers import generate_session_id, format_results
from config.logging_config import setup_logging
from config.settings import OPENAI_API_KEY

def main(task: str, initial_context: str = "") -> Dict[str, Any]:
    """
    Run the LangGraph application with the given task.
    
    Args:
        task: The task to perform
        initial_context: Any initial context to provide
        
    Returns:
        The final state after completion
    """
    # Set up logging
    logger = setup_logging()
    logger.info(f"Starting application with task: {task}")
    
    # Ensure API key is set
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY not set. Please set it in .env file or environment variables.")
        sys.exit(1)
    
    # Create the graph
    logger.info("Creating graph")
    graph = create_main_graph()
    
    # Generate session ID
    session_id = generate_session_id()
    logger.info(f"Session ID: {session_id}")
    
    # Initialize state
    initial_state = AppState(
        messages=[],
        context=initial_context,
        task=task,
        plan=None,
        results=None,
        status="initialized",
        error=None
    )
    
    # Run the application
    logger.info("Running graph")
    try:
        final_state = graph.invoke(initial_state)
        logger.info("Graph execution completed successfully")
        
        # Format and log results
        if final_state.get("results"):
            formatted_results = format_results(final_state["results"])
            logger.info(f"Results:\n{formatted_results}")
        
        return final_state
        
    except Exception as e:
        logger.error(f"Error during graph execution: {str(e)}")
        return {
            "error": str(e),
            "status": "failed",
            "messages": initial_state["messages"] + [{"role": "system", "content": f"Error: {str(e)}"}]
        }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run LangGraph application")
    parser.add_argument("--task", required=True, help="The task to perform")
    parser.add_argument("--context", default="", help="Initial context for the task")
    
    args = parser.parse_args()
    
    result = main(args.task, args.context)
    
    # Print final messages
    for msg in result.get("messages", []):
        if msg["role"] != "system":
            print(f"{msg['role'].capitalize()}: {msg['content']}")

