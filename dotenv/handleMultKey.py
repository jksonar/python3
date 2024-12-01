# Handle Multiple Keys with Similar Names
from dotenv import load_dotenv
import os

load_dotenv()

keys = [key for key in os.environ if "DB_" in key]
print(keys)
