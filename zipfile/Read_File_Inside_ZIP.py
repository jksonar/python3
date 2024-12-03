# Read a File Inside ZIP Without Extracting
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    with zipf.open('file1.txt') as file:
        print(file.read().decode())
