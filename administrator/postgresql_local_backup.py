import os
import time
import logging
from datetime import date
import calendar
from pathlib import Path
from subprocess import Popen, PIPE
from zipfile import ZipFile
import shutil

# script is improved by chatgpt
# Constants
DB_COMMAND = "d:\\iso\\pgsql\\bin\\pg_dump.exe"
BACKUP_DIR = Path("D:\\")
WEEKLY_BACKUP_DIR = BACKUP_DIR / "weekly"
DELETE_DIR = Path("D:\\DATA\\docker\\multidocker")
LOG_DIR = BACKUP_DIR
RETENTION_DAYS = 7
WEEKLY_RETENTION_DAYS = 20
PGPASSWORD = "TomAndJ3rry"
os.environ["PGPASSWORD"] = PGPASSWORD

DB_NAME = "jksonar"
PHOST = "192.168.56.145"
PORT = "5432"
PUSER = "jay"

# Logging setup
date_uniq = time.strftime("%Y_%m_%d_%H_%M")
log_file = LOG_DIR / f"dbscript_{date_uniq}.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Functions
def create_zip(backup_file, is_weekly=False):
    """Create a zip file for the backup."""
    zip_file_name = f"{backup_file}.zip"
    weekly_zip_file_name = WEEKLY_BACKUP_DIR / f"dedivipu_db1_{backup_file.stem}.zip"

    try:
        with ZipFile(zip_file_name, 'w') as zipf:
            zipf.write(backup_file, arcname=backup_file.name)
        backup_file.unlink()  # Delete the original SQL file after zipping
        logging.info(f"Backup zipped: {zip_file_name}")

        # Copy to weekly backup if it's Wednesday
        if is_weekly:
            shutil.copyfile(zip_file_name, weekly_zip_file_name)
            logging.info(f"Weekly backup created: {weekly_zip_file_name}")

    except Exception as e:
        logging.error(f"Failed to create zip file: {e}")

def delete_old_files(directory, retention_days):
    """Delete files older than retention_days."""
    current_time = time.time()
    try:
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".zip":
                creation_time = file.stat().st_ctime
                if (current_time - creation_time) // (24 * 3600) >= retention_days:
                    file.unlink()
                    logging.info(f"Deleted old backup: {file}")
    except Exception as e:
        logging.error(f"Error deleting old files in {directory}: {e}")

def backup_database():
    """Run the pg_dump command to back up the database."""
    backup_file = BACKUP_DIR / f"{DB_NAME}_{date_uniq}.sql"
    try:
        command = [DB_COMMAND, "-h", PHOST, "-p", PORT, "-U", PUSER, "-d", DB_NAME, "-f", str(backup_file)]
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            logging.info(f"Backup successful: {backup_file}")
            return backup_file
        else:
            logging.error(f"Backup failed: {stderr.decode()}")
            return None
    except Exception as e:
        logging.error(f"Error running pg_dump: {e}")
        return None

# Main execution
if __name__ == "__main__":
    logging.info("Starting backup script.")

    # Backup the database
    backup_file = backup_database()
    if backup_file:
        today_is = calendar.day_name[date.today().weekday()]
        is_weekly = (today_is == "Wednesday")
        create_zip(backup_file, is_weekly=is_weekly)

    # Delete old backups
    delete_old_files(DELETE_DIR, RETENTION_DAYS)
    delete_old_files(WEEKLY_BACKUP_DIR, WEEKLY_RETENTION_DAYS)

    logging.info("Backup script completed.")
