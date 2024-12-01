# Precedence of Variables
from dotenv import load_dotenv
import os

os.environ["API_KEY"] = "existing_value"
load_dotenv(override=False)  # Keeps the existing value
print(os.getenv("API_KEY"))
