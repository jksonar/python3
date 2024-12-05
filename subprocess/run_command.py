# Run Command with Both stdout and stderr
import subprocess

result = subprocess.run(["ls", "nonexistent_file"], capture_output=True, text=True)
print("Output:", result.stdout)
print("Error:", result.stderr)
