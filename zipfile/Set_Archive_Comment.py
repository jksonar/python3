# Set Archive Comment
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.comment = b"This is a ZIP archive."
