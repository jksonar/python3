# Use os.environ Directly
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["NEW_VAR"] = "new_value"
print(os.getenv("NEW_VAR"))
