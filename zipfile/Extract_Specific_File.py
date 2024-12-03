# Extract Specific File
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extract('file1.txt', 'output_folder')
print("File extracted.")
