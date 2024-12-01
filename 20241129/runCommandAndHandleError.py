# Run a Command and Handle Errors
import subprocess
try:
    subprocess.run(["cat", "nonexistent_file.txt"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with error:", e)
