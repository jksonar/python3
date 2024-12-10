
# Checking if a File is in a TAR Archive

import tarfile

with tarfile.open("example.tar", "r") as tar:
    if "file1.txt" in tar.getnames():
        print("file1.txt is in the archive.")
