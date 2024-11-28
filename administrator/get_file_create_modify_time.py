import os
import time

file_path = "example.txt"
creation_time = os.path.getctime(file_path)
modification_time = os.path.getmtime(file_path)

print("Creation Time:", time.ctime(creation_time))
print("Modification Time:", time.ctime(modification_time))
