# Check Output of a Command
import subprocess
output = subprocess.check_output(["ls", "-l"])
print(output.decode())
