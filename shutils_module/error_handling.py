import shutil

try:
    shutil.copy("nonexistent_file.txt", "destination.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")
