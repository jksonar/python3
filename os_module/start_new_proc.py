# Spawn a New Process
import os

os.spawnlp(os.P_NOWAIT, 'python3', 'python3', '-c', 'print("Hello, World!")')
