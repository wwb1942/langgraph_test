# app/tools/data_tools.py
import json
from typing import Any, Dict

def process_data(data: str) -> Dict[str, Any]:
    """Process raw data from execution into structured format."""
    # Try to parse as JSON
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        # If not JSON, return as text
        return {"text": data.strip()}

def save_results(results: Dict[str, Any], filename: str) -> str:
    """Save results to output file."""
    output_path = f"data/output/{filename}"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    return output_path
