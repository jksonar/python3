import subprocess
# Handling Errors Gracefully

source = "/invalid/source/"
destination = "/path/to/destination/"

try:
    subprocess.run(["rsync", "-avz", source, destination], check=True)
    print("Sync successful!")
except subprocess.CalledProcessError as e:
    print("Error occurred:", e.stderr)
