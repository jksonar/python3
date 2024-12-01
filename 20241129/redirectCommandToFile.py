# Redirect Command Output to a File
import subprocess
with open("output.txt", "w") as f:
    subprocess.run(["ls", "-l"], stdout=f)
print("Output saved to file.")
