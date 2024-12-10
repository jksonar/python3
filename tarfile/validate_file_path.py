# Extracting Members Safely

# To avoid unsafe file paths (e.g., paths with .. or absolute paths), validate file paths before extraction:

import os
import tarfile

def is_safe_path(base_path, target_path):
    abs_base = os.path.abspath(base_path)
    abs_target = os.path.abspath(target_path)
    return abs_target.startswith(abs_base)

with tarfile.open("example.tar", "r") as tar:
    for member in tar.getmembers():
        target_path = os.path.join("output_directory", member.name)
        if is_safe_path("output_directory", target_path):
            tar.extract(member, path="output_directory")
