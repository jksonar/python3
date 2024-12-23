import shutil

def backup_files(src, dest):
    try:
        shutil.copytree(src, dest)
        print(f"Backup successful from {src} to {dest}")
    except Exception as e:
        print(f"Error: {e}")

backup_files("/etc", "/backup/etc")
