import shutil

def copy_if_enough_space(src, dst):
    free_space = shutil.disk_usage(dst).free
    file_size = os.path.getsize(src)
    if free_space > file_size:
        shutil.copy(src, dst)
        print("File copied successfully.")
    else:
        print("Not enough disk space!")

copy_if_enough_space("large_file.txt", "/destination_folder")
