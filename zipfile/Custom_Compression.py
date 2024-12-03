# Add Files with Custom Compression
import zipfile

with zipfile.ZipFile('example.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('file1.txt')
