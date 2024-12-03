# Compress Without Relative Paths
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file1.txt', arcname='file1.txt')  # Exclude folder structure
