# Run a Command with Timeout
import subprocess

try:
    subprocess.run(["sleep", "5"], timeout=2)
except subprocess.TimeoutExpired:
    print("Command timed out!")
