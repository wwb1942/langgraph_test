# app/utils/helpers.py
import json
from typing import Dict, Any, List
import hashlib

def generate_session_id() -> str:
    """Generate a unique session ID based on timestamp."""
    import time
    timestamp = str(time.time())
    return hashlib.md5(timestamp.encode()).hexdigest()[:10]

def format_results(results: Dict[str, Any]) -> str:
    """Format execution results for display."""
    output = []
    for key, value in results.items():
        if isinstance(value, dict):
            formatted_value = json.dumps(value, indent=2)
        else:
            formatted_value = str(value)
        
        output.append(f"## {key}\n{formatted_value}\n")
    
    return "\n".join(output)

def extract_plan_from_text(text: str) -> List[str]:
    """Extract numbered plan items from text."""
    import re
    # Look for numbered items like "1. Do something"
    plan_items = re.findall(r"\d+\.\s+(.*?)(?=\n\d+\.|\n\n|$)", text, re.DOTALL)
    return [item.strip() for item in plan_items]
