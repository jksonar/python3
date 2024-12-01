# Temporarily Override Variables
from dotenv import load_dotenv
import os

load_dotenv()

original = os.getenv("API_KEY")
os.environ["API_KEY"] = "temporary_value"
print("Temporary:", os.getenv("API_KEY"))
os.environ["API_KEY"] = original
