# Combine .env Variables
from dotenv import load_dotenv
import os

load_dotenv()

combined = f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
print(f"Combined Host and Port: {combined}")
