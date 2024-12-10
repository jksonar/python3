# Adding Files to an Existing TAR Archive
import tarfile

with tarfile.open("example.tar", "a") as tar:
    tar.add("new_file.txt")
