# Communicate with a Process
import subprocess

process = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
output, _ = process.communicate(input="Hello, World!")
print(output)
