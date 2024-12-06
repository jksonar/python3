# Using a Python Wrapper for Rsync
import subprocess

def rsync(source, destination, options=None):
    command = ["rsync", "-avz"]
    if options:
        command.extend(options)
    command.extend([source, destination])
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Sync successful!")
        print(result.stdout)
    else:
        print("Error:", result.stderr)

# Example usage
rsync("/path/to/source/", "/path/to/destination/", options=["--delete"])
