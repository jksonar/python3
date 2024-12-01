from dotenv import unset_key, load_dotenv

load_dotenv()

unset_key(".env", "UNUSED_KEY")
print("Variable removed from .env")
# Delete a Key from .env