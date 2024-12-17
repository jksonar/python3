# MD5 Checksum Code for All Files in a Directory
import hashlib
from pathlib import Path

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def calculate_md5_for_directory(directory):
    """Calculate MD5 checksum for all files in a directory."""
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Invalid directory: {directory}")
        return
    
    print(f"Scanning directory: {directory}\n")
    for file in directory.rglob("*"):
        if file.is_file():
            md5 = calculate_md5(file)
            if md5:
                print(f"{file}: {md5}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ").strip()
    calculate_md5_for_directory(dir_path)
