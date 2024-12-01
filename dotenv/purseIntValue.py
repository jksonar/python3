# Parse Integer Values
from dotenv import load_dotenv
import os

load_dotenv()

db_port = int(os.getenv("DB_PORT", "5432"))
print(f"Database Port: {db_port}")
