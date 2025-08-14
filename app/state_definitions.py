# app/state_definitions.py
from typing import TypedDict, List, Optional, Dict, Any

class AppState(TypedDict):
    """State definition for the main application."""
    messages: List[Dict[str, Any]]  # Chat history
    context: str                    # Research context
    task: str                       # Current task
    plan: Optional[List[str]]       # Task plan
    results: Optional[Dict[str, Any]]  # Execution results
    status: str                     # Current status (e.g., "researching", "planning")
    error: Optional[str]            # Error message if any
