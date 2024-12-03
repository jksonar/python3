# Password-Protected ZIP
import zipfile

with zipfile.ZipFile('protected.zip') as zipf:
    zipf.extractall(pwd=b'mypassword')
