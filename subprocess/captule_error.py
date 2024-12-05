# Capture Error Output
import subprocess

result = subprocess.run(["ls", "nonexistent_file"], capture_output=True, text=True)
print("Error:", result.stderr)
