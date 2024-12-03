# Get Archive Comment
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    print(zipf.comment.decode())
