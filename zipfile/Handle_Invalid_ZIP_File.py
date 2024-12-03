# Handle Invalid ZIP File
import zipfile

try:
    with zipfile.ZipFile('corrupt.zip', 'r') as zipf:
        zipf.extractall('output')
except zipfile.BadZipFile:
    print("Invalid ZIP file.")
