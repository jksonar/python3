# Export Variables to Subprocess
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

result = subprocess.run(["echo", os.getenv("API_KEY")], capture_output=True)
print(result.stdout.decode())
