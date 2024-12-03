# Extract Files Securely
import os
import zipfile

def safe_extract(zip_file, path):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        for member in zipf.namelist():
            dest = os.path.join(path, member)
            if not os.path.abspath(dest).startswith(os.path.abspath(path)):
                raise Exception("Attempted Path Traversal in ZIP File")
        zipf.extractall(path)

safe_extract('example.zip', 'output_folder')
