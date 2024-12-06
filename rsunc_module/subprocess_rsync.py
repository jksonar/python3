# Using subprocess to Run rsync ; Basic rsync Command

import subprocess

source = "/path/to/source/"
destination = "/path/to/destination/"

result = subprocess.run(["rsync", "-avz", source, destination], capture_output=True, text=True)
if result.returncode == 0:
    print("Sync successful!")
else:
    print("Sync failed:", result.stderr)
