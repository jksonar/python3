# Pass Input to a Command
import subprocess

result = subprocess.run(["cat"], input="Hello, World!", capture_output=True, text=True)
print(result.stdout)  # Output: Hello, World!
