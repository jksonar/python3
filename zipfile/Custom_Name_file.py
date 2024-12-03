# Add a File with a Custom Name
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file1.txt', 'renamed_file.txt')
