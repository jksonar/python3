# Include Specific Files
import subprocess

source = "/path/to/source/"
destination = "/path/to/destination/"

result = subprocess.run([
    "rsync", "-avz", "--include", "*.txt", "--exclude", "*", source, destination
], capture_output=True, text=True)
print(result.stdout)
