# Listing Contents of a TAR File
import tarfile

with tarfile.open("example.tar", "r") as tar:
    for member in tar.getmembers():
        print(member.name)
