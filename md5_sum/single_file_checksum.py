# MD5 Checksum Code for a Single File
import hashlib

def calculate_md5(file_path):
    """Calculate MD5 checksum for a single file."""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error calculating MD5 for {file_path}: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ").strip()
    md5sum = calculate_md5(file_path)
    if md5sum:
        print(f"MD5 Checksum: {md5sum}")
