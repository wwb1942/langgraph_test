# app/tools/web_tools.py
import requests
from typing import Dict, Any, Optional

def fetch_web_data(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Fetch data from web API."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "error": str(e)}
