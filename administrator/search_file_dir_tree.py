import os

def find_file(root_dir, filename):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

file_path = find_file("/", "example.txt")
if file_path:
    print("File Found:", file_path)
else:
    print("File Not Found")
