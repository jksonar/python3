# Write Variables to .env
from dotenv import set_key, load_dotenv

load_dotenv()

set_key(".env", "NEW_VAR", "value")
print("Variable written to .env")
