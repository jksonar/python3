# Split a Path into Directory and File
import os

directory, file = os.path.split('/path/to/file.txt')
print("Directory:", directory)
print("File:", file)
