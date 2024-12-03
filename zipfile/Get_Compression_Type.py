# Get Compression Type
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    for file in zipf.infolist():
        print(f"{file.filename}: {file.compress_type}")
