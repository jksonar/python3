# Run Command and Handle Errors
import subprocess

try:
    subprocess.run(["ls", "nonexistent_file"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with return code", e.returncode)
