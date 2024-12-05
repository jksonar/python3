# Debugging Commands

# To debug subprocess calls, print the args, stdout, and stderr fields of the CompletedProcess object returned by subprocess.run()

import subprocess

result = subprocess.run(["ls", "nonexistent_file"], capture_output=True, text=True)
print("Args:", result.args)
print("Return Code:", result.returncode)
print("Stdout:", result.stdout)
print("Stderr:", result.stderr)
