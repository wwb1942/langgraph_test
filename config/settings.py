# config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
TIMEOUT = int(os.getenv("TIMEOUT", "60"))

# Data paths
INPUT_DIR = os.getenv("INPUT_DIR", "data/input")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")
