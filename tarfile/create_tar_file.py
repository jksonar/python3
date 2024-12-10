# Creating a TAR Archive
import tarfile

# Create a .tar File
with tarfile.open("example.tar", "w") as tar:
    tar.add("file1.txt")  # Add a single file
    tar.add("folder")     # Add a folder and its contents recursively

# Create a Compressed .tar.gz File
with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("file1.txt")
    tar.add("folder")

# Create a Compressed .tar.bz2 File
with tarfile.open("example.tar.bz2", "w:bz2") as tar:
    tar.add("file1.txt")
    tar.add("folder")
