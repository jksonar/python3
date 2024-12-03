# Open ZIP File Without Context Manager
import zipfile

zipf = zipfile.ZipFile('example.zip', 'r')
print(zipf.namelist())
zipf.close()
