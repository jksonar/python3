# Extracting a TAR Archive
import tarfile

# Extract All Files
with tarfile.open("example.tar", "r") as tar:
    tar.extractall("output_directory")  # Specify directory or use default

# Extract a Specific File
with tarfile.open("example.tar", "r") as tar:
    tar.extract("file1.txt", path="output_directory")
