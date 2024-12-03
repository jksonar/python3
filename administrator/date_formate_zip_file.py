# programe to take zip of passwd file
# file name added Date and time 
import zipfile
from datetime import datetime

today = datetime.now()
FileName = input("Please Enter File name: ")

with zipfile.ZipFile(f"{FileName}_{today.year}{today.month}{today.day}{today.hour}{today.minute}.zip", 'w') as zipf:
    zipf.write('/etc/passwd')
    zipf.write('/etc/group')
print("ZIP file created.")