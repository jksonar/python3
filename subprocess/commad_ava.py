# Check Command Availability
import subprocess

result = subprocess.run(["which", "python3"], capture_output=True, text=True)
if result.returncode == 0:
    print("Python3 is available at:", result.stdout.strip())
else:
    print("Python3 is not available.")
