import os
file_path = "example.txt"

print("Readable:", os.access(file_path, os.R_OK))
print("Writable:", os.access(file_path, os.W_OK))
print("Executable:", os.access(file_path, os.X_OK))
