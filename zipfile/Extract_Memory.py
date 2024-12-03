# Extract to Memory
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    data = zipf.read('file1.txt')
    print(data.decode())
