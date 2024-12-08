# Move All Files of a Specific Type
import shutil
import os

def move_files_by_type(source_dir, destination_dir, file_extension):
    os.makedirs(destination_dir, exist_ok=True)
    for file_name in os.listdir(source_dir):
        if file_name.endswith(file_extension):
            shutil.move(os.path.join(source_dir, file_name), destination_dir)

move_files_by_type("source_folder", "destination_folder", ".txt")

# Back Up a Directory
import shutil

shutil.copytree("source_directory", "backup_directory")


# Clean Up a Directory
import shutil

shutil.rmtree("old_directory")
