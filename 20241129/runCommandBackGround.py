# Run Command in Background
import subprocess
process = subprocess.Popen(["sleep", "5"])
print("Sleeping...")
process.wait()
print("Done.")
