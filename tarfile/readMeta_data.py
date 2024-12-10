# Reading File Metadata
import tarfile

with tarfile.open("example.tar", "r") as tar:
    for member in tar.getmembers():
        print(f"Name: {member.name}")
        print(f"Size: {member.size} bytes")
        print(f"Modified: {member.mtime}")
        print("-" * 20)
