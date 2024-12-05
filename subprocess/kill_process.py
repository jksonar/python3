# Kill a Process
import subprocess
import time

process = subprocess.Popen(["sleep", "10"])
time.sleep(2)
process.terminate()
print("Process terminated.")
