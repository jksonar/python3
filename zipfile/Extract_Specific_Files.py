# Extract Specific Files by Pattern
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zipf:
    for file in zipf.namelist():
        if file.endswith('.txt'):
            zipf.extract(file, 'output_folder')
print("TXT files extracted.")
