# Create a New ZIP File
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')
print("ZIP file created.")
