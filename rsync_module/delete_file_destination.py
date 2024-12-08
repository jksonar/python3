# Delete Extra Files at Destination
import subprocess

source = "/path/to/source/"
destination = "/path/to/destination/"

result = subprocess.run(["rsync", "-avz", "--delete", source, destination], capture_output=True, text=True)
if result.returncode == 0:
    print("Sync completed with delete!")
else:
    print("Error:", result.stderr)
