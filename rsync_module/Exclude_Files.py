# Exclude Files
import subprocess

source = "/path/to/source/"
destination = "/path/to/destination/"
exclude_pattern = "*.log"  # Example: exclude all .log files

result = subprocess.run(["rsync", "-avz", "--exclude", exclude_pattern, source, destination], capture_output=True, text=True)
print(result.stdout)
