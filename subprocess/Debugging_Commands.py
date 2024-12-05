# Debugging Commands
import subprocess

result = subprocess.run(["ls", "nonexistent_file"], capture_output=True, text=True)
print("Args:", result.args)
print("Return Code:", result.returncode)
print("Stdout:", result.stdout)
print("Stderr:", result.stderr)
