import os
path = "/path/to/file/example.txt"
directory, file = os.path.split(path)
print("Directory:", directory)
print("File:", file)
