# Extract Password-Protected ZIP
import pyminizip
# pip install pyminizip
import zipfile

with zipfile.ZipFile('protected.zip', 'r') as zipf:
    zipf.extractall(pwd=b'password')
