# Dry Run to Preview Changes
import subprocess

source = "/path/to/source/"
destination = "/path/to/destination/"

result = subprocess.run(["rsync", "-avz", "--dry-run", source, destination], capture_output=True, text=True)
print("Dry Run Output:\n", result.stdout)
