# Delete a File from ZIP
import zipfile

def remove_file_from_zip(zip_name, file_to_remove):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        files = [f for f in zipf.namelist() if f != file_to_remove]
        with zipfile.ZipFile('new_' + zip_name, 'w') as new_zipf:
            for file in files:
                new_zipf.writestr(file, zipf.read(file))

remove_file_from_zip('example.zip', 'file1.txt')
