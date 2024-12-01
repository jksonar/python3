# Load Variables from a .env File
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")
