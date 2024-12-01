# Check if a Variable is Loaded
from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("API_KEY"):
    raise ValueError("API_KEY is not set in the environment.")
