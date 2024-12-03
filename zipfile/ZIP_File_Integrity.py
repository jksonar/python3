# Test ZIP File Integrity
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    if zipf.testzip() is None:
        print("ZIP file is intact.")
    else:
        print("ZIP file is corrupted.")
