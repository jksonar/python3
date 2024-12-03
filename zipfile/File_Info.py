# Get File Info
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    info = zipf.getinfo('file1.txt')
    print(f"File name: {info.filename}")
    print(f"Compressed size: {info.compress_size}")
    print(f"Original size: {info.file_size}")
