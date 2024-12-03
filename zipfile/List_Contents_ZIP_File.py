# List Contents of a ZIP File
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    print(zipf.namelist())
