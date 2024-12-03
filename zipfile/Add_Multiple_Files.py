# Add Multiple Files
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    for file in files:
        zipf.write(file)
