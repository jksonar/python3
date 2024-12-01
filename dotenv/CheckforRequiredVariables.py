# Check for Required Variables
from dotenv import load_dotenv
import os

load_dotenv()

required_keys = ["DB_HOST", "DB_PORT", "DB_USER"]
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise EnvironmentError(f"Missing keys: {missing_keys}")
