# Update File in ZIP
import zipfile

def update_file_in_zip(zip_name, file_name, new_content):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        files = {f: zipf.read(f) for f in zipf.namelist()}
        files[file_name] = new_content
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for f, content in files.items():
            zipf.writestr(f, content)

update_file_in_zip('example.zip', 'file1.txt', b'Updated content')
