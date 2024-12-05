# Suppress Output
import subprocess

subprocess.run(["echo", "This will not show"], stdout=subprocess.DEVNULL)
