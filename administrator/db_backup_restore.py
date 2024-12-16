# 1. read ini file db_backup.ini
# 2. take backup of MySQL , PostgreSQL databases backup
# 3. take daly backup or weekly backup
# 4. copy backup files to remote server
# 5. remove old backup files base on retention from remote and local

import configparser
import os
from subprocess import Popen, PIPE
import time
import logging
from datetime import date
import calendar
from pathlib import Path
from subprocess import Popen, PIPE
from zipfile import ZipFile
import shutil

# reading ini file 
config = configparser.ConfigParser()
FilePath = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
iniFileName = os.path.join(FilePath, 'db_backup.ini')
config.read(iniFileName)

# details for database
DATABASE = config['DEFAULT']['DATABASE']
HOST = config['DEFAULT']['HOST']
PORT = config['DEFAULT']['PORT']
USER = config['DEFAULT']['USER']
BACKUP_DIR = config['DEFAULT']['BACKUP_DIR']

DATE_UNIQ = time.strftime("%Y_%m_%d_%H_%M")
LOG_DIR = config['DEFAULT']['LOG_DIR']
LOG_FILE_NAME = LOG_DIR / f"dbscript_{DATE_UNIQ}.log"
DATABASE_FILE_NAME = os.path.join(BACKUP_DIR,f"{DATABASE}_{DATE_UNIQ}.sql")
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

RETENTION_DAYS = config['retention']['RETENTION_DAYS']
WEEKLY_RETENTION_DAYS = config['retention']['WEEKLY_RETENTION_DAYS']
WEEKLY_BACKUP_DIR = BACKUP_DIR / "weekly"

# if condition for mysql command
if 'mysql' == config['DEFAULT']['DB_ENGIN']:
    pass

#if condition for copy backup to remote using ssh 
if config['DEFAULT']['copy_remote_ssh']:
    pass

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
    backup_file = BACKUP_DIR / f"{DATABASE}_{DATE_UNIQ}.sql"
    try:
        if 'postgres' == config['DEFAULT']['DB_ENGIN']:
            os.environ["PGPASSWORD"] = config['DEFAULT']['PASSWORD']
            result = Popen(["pg_dump", "-h", HOST, "-U", USER, "-d", DATABASE, "-f", DATABASE_FILE_NAME],stdout=PIPE, stderr=PIPE)
            stdout, stderr = result.communicate()

        elif 'mysql' == config['DEFAULT']['DB_ENGIN']:
            PASSWORD = config['DEFAULT']['PASSWORD']
            # --result-file=backup.sql
            result = Popen(["mysqldump","-h",HOST,"-P",PORT,"-u",USER,"-p",PASSWORD,">",DATABASE_FILE_NAME],stdout=PIPE, stderr=PIPE)
            stdout, stderr = result.communicate()

        if result.returncode == 0:
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
    delete_old_files(BACKUP_DIR, RETENTION_DAYS)
    delete_old_files(WEEKLY_BACKUP_DIR, WEEKLY_RETENTION_DAYS)

    logging.info("Backup script completed.")