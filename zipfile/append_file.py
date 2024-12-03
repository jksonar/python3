# Append to an Existing ZIP File
import zipfile

with zipfile.ZipFile('example.zip', 'a') as zipf:
    zipf.write('file3.txt')
print("File added to ZIP.")
