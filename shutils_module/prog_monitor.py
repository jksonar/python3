# Progress Monitoring for Copy Operations
# Copy a File with Progress Callback

# Use shutil.copyfileobj for custom operations

import shutil

def copy_with_progress(src, dst):
    with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
        shutil.copyfileobj(fsrc, fdst, length=1024*1024)  # Copy in chunks (1 MB)

copy_with_progress("large_file.txt", "destination.txt")
