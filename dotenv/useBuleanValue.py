# Use Boolean Values from .env
from dotenv import load_dotenv
import os

load_dotenv()

debug_mode = os.getenv("DEBUG", "false").lower() == "true"
print(f"Debug Mode: {debug_mode}")
