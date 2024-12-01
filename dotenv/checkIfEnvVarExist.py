# Check if an Environment Variable Exists
from dotenv import load_dotenv
import os

load_dotenv()

if "API_KEY" in os.environ:
    print("API_KEY is set!")
else:
    print("API_KEY is missing.")
