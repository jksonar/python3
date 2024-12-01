# Load Variables Dynamically
from dotenv import load_dotenv
import os

def load_and_print_env(file_path):
    load_dotenv(dotenv_path=file_path)
    print(os.getenv("DYNAMIC_VAR"))

load_and_print_env(".env")
