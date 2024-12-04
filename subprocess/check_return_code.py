# Check Return Code
import subprocess

result = subprocess.run(["ls", "nonexistent_file"], capture_output=True, text=True)
if result.returncode != 0:
    print("Command failed:", result.stderr)
