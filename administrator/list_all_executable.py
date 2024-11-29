import os

path = "."
executables = [f for f in os.listdir(path) if os.access(f, os.X_OK) and os.path.isfile(f)]
print("Executable Files:", executables)
