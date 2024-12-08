# Temporary Directories

# Use shutil with tempfile to create temporary directories.

import tempfile
import shutil

with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at {temp_dir}")
    # Perform operations in temp_dir
# Directory is automatically cleaned up
