# The pathlib module in Python provides an object-oriented interface for working with file system paths. 
# It simplifies many common file system tasks, such as creating, reading, and deleting files or directories.

# Create a Path Object

from pathlib import Path
import time

# Create a Path object for a file or directory
file_path = Path("example.txt")
dir_path = Path("/home/user/documents")

# Check If a Path Exists
if file_path.exists():
    print(f"{file_path} exists")
else:
    print(f"{file_path} does not exist")

# Create a Directory
# Create a single directory
Path("new_directory").mkdir(exist_ok=True)

# Create nested directories
Path("nested/dir/path").mkdir(parents=True, exist_ok=True)

# Iterate Through a Directory
# List all files and directories in a directory
for item in Path(".").iterdir():
    print(item)

# List only files
for file in Path(".").iterdir():
    if file.is_file():
        print(file)

#  Check File or Directory
if file_path.is_file():
    print(f"{file_path} is a file")
elif file_path.is_dir():
    print(f"{file_path} is a directory")

# Get File Name, Extension, and Parent Directory
path = Path("/home/user/example.txt")

# Get the file name
print(path.name)  # example.txt

# Get the file stem (name without extension)
print(path.stem)  # example

# Get the file extension
print(path.suffix)  # .txt

# Get the parent directory
print(path.parent)  # /home/user

# Combine Paths
base_path = Path("/home/user")
full_path = base_path / "documents" / "file.txt"
print(full_path)  # /home/user/documents/file.txt

# Read and Write to a File
# Write to a file
file_path.write_text("Hello, World!", encoding="utf-8")

# Read from a file
content = file_path.read_text(encoding="utf-8")
print(content)

# Rename or Move a File
file_path.rename("new_example.txt")  # Rename file
file_path.replace("moved_example.txt")  # Move file

# Delete Files and Directories
# Delete a file
file_path.unlink(missing_ok=True)

# Delete a directory
Path("new_directory").rmdir()

# Get Absolute Path
absolute_path = file_path.resolve()
print(absolute_path)

# Match Files Using Wildcards
# Match all .txt files in the current directory
for txt_file in Path(".").glob("*.txt"):
    print(txt_file)

# Recursively match all .py files
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Check File Size
file_size = file_path.stat().st_size
print(f"File size: {file_size} bytes")

# Working with Home Directory
# Get the home directory
home = Path.home()
print(home)

# Create a path in the home directory
desktop = home / "Desktop"
print(desktop)

# Copy or Move Files
# Although pathlib doesn't directly support copy operations, you can use it with shutil:
import shutil

source = Path("example.txt")
destination = Path("backup/example.txt")

# Copy a file
shutil.copy2(source, destination)

# Move a file
shutil.move(source, destination)

# File Creation Date
file_creation_time = file_path.stat().st_ctime
print(f"File creation time: {time.ctime(file_creation_time)}")

# Compare Paths
path1 = Path("example.txt")
path2 = Path("./example.txt")

# Compare paths
if path1 == path2:
    print("Paths are the same")

# Check File Permissions
# Check if a file is readable, writable, or executable
print(file_path.is_readable())
print(file_path.is_writable())
print(file_path.is_executable())

# Get All Parent Directories
path = Path("/home/user/documents/file.txt")

# Iterate over all parent directories
for parent in path.parents:
    print(parent)

# Temporary Files with Pathlib
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    temp_path = Path(temp_dir)
    temp_file = temp_path / "temp_file.txt"
    temp_file.write_text("Temporary data")
    print(temp_file.read_text())
# Temporary directory and files are deleted automatically

# Check Symbolic Links
if file_path.is_symlink():
    print(f"{file_path} is a symbolic link")

# pathlib is powerful and integrates seamlessly with many modern Python libraries. 
# It is highly recommended for any file or path-related tasks in Python