# Specify a Custom .env File
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="custom.env")

db_host = os.getenv("DB_HOST")
print(f"Database Host: {db_host}")
