import os

def find_large_files(path="/", size_limit=100):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_limit * 1024 * 1024:
                print(f"{file_path} - {os.path.getsize(file_path) // (1024**2)} MB")

find_large_files("/", 500)
