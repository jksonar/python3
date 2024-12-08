# Sync Over SSH
import subprocess

source = "/path/to/source/"
destination = "user@remote_host:/path/to/destination/"

result = subprocess.run(["rsync", "-avz", "-e", "ssh", source, destination], capture_output=True, text=True)
if result.returncode == 0:
    print("Sync successful!")
else:
    print("Error:", result.stderr)
