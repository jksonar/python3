# Extract All Files
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('output_folder')
print("Files extracted.")
