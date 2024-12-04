# Redirect Output to a File
import subprocess

with open("output.txt", "w") as f:
    subprocess.run(["echo", "Hello, File!"], stdout=f)
