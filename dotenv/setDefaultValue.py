# Set Default Values if Variable is Missing
from dotenv import load_dotenv
import os

load_dotenv()

db_port = os.getenv("DB_PORT", "3306")  # Default to 3306 if not set
print(f"Database Port: {db_port}")
