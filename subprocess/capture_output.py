# Capture Output of a Command
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)  # Prints the command output
