import glob

# Use with os for Metadata

import os

for file in glob.glob("*.txt"):
    print(f"File: {file}, Size: {os.path.getsize(file)} bytes")

# b. Copy Matching Files

import shutil

for file in glob.glob("*.txt"):
    shutil.copy(file, "backup/")  # Copy each `.txt` file to the `backup` folder
