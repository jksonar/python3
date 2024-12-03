# Archive Empty Folder
import os
import zipfile

os.makedirs('empty_folder', exist_ok=True)
with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('empty_folder', arcname='empty_folder/')
