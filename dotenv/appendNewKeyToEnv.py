# Append a New Key-Value Pair to .env
from dotenv import set_key

set_key(".env", "NEW_SETTING", "enabled")
print("Added to .env")
