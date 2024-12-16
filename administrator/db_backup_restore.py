# 1. read ini file db_backup.ini
# 2. take backup of MySQL , PostgreSQL databases backup
# 3. take daly backup or weekly backup
# 4. copy backup files to remote server
# 5. remove old backup files base on retention from remote and local

import configparser
import os
import time
import logging
from datetime import date
import calendar
from pathlib import Path
from zipfile import ZipFile
import shutil
from subprocess import Popen, PIPE

# Constants for database engines
DB_POSTGRES = "postgres"
DB_MYSQL = "mysql"

def load_config(file_path):
    """Load and validate configuration from an INI file."""
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    config.read(file_path)
    return config

def setup_logging(log_dir, date_uniq):
    """Set up logging to a file."""
    log_dir_path = Path(log_dir)
    log_dir_path.mkdir(parents=True, exist_ok=True)
    log_file_name = log_dir_path / f"dbscript_{date_uniq}.log"
    logging.basicConfig(
        filename=log_file_name, 
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging initialized.")
    return log_file_name

def validate_directories(directories):
    """Ensure required directories exist."""
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

def create_zip(backup_file, weekly_backup_dir, is_weekly=False):
    """Create a zip file for the backup."""
    zip_file_name = f"{backup_file}.zip"
    try:
        with ZipFile(zip_file_name, 'w') as zipf:
            zipf.write(backup_file, arcname=Path(backup_file).name)
        Path(backup_file).unlink()  # Delete the original SQL file after zipping
        logging.info(f"Backup zipped: {zip_file_name}")

        if is_weekly:
            weekly_zip_file_name = Path(weekly_backup_dir) / f"{Path(backup_file).stem}.zip"
            shutil.copy2(zip_file_name, weekly_zip_file_name)
            logging.info(f"Weekly backup created: {weekly_zip_file_name}")

    except Exception as e:
        logging.error(f"Failed to create zip file: {e}")

def delete_old_files(directory, retention_days):
    """Delete files older than the retention period."""
    current_time = time.time()
    for file in Path(directory).iterdir():
        if file.is_file() and file.suffix == ".zip":
            creation_time = file.stat().st_ctime
            if (current_time - creation_time) // (24 * 3600) >= retention_days:
                try:
                    file.unlink()
                    logging.info(f"Deleted old backup: {file}")
                except Exception as e:
                    logging.error(f"Failed to delete file {file}: {e}")

def backup_database(config, backup_file):
    """Run the database dump command."""
    db_engine = config['DEFAULT']['DB_ENGIN'].lower()
    try:
        if db_engine == DB_POSTGRES:
            os.environ["PGPASSWORD"] = config['DEFAULT']['PASSWORD']
            result = Popen(
                ["pg_dump", "-h", config['DEFAULT']['HOST'], "-p", config['DEFAULT']['PORT'], 
                 "-U", config['DEFAULT']['USER'], "-d", config['DEFAULT']['DATABASE'], 
                 "-f", backup_file],
                stdout=PIPE, stderr=PIPE
            )

        elif db_engine == DB_MYSQL:
            result = Popen(
                ["mysqldump", "-h", config['DEFAULT']['HOST'], "-P", config['DEFAULT']['PORT'], 
                 "-u", config['DEFAULT']['USER'], f"--password={config['DEFAULT']['PASSWORD']}", 
                 "--result-file", backup_file],
                stdout=PIPE, stderr=PIPE
            )

        stdout, stderr = result.communicate()
        if result.returncode == 0:
            logging.info(f"Backup successful: {backup_file}")
            return backup_file
        else:
            logging.error(f"Backup failed: {stderr.decode()}")
            return None

    except Exception as e:
        logging.error(f"Error during backup: {e}")
        return None

def main():
    """Main function to execute the backup process."""
    try:
        # Load configuration
        config = load_config("db_backup.ini")
        date_uniq = time.strftime("%Y_%m_%d_%H_%M")
        backup_dir = Path(config['DEFAULT']['BACKUP_DIR'])
        log_dir = config['DEFAULT']['LOG_DIR']
        weekly_backup_dir = backup_dir / "weekly"
        validate_directories([backup_dir, log_dir, weekly_backup_dir])

        # Set up logging
        setup_logging(log_dir, date_uniq)

        # Backup database
        backup_file = backup_dir / f"{config['DEFAULT']['DATABASE']}_{date_uniq}.sql"
        backup_file_path = backup_database(config, backup_file)

        if backup_file_path:
            today_is = calendar.day_name[date.today().weekday()]
            is_weekly = (today_is == "Wednesday")
            create_zip(backup_file_path, weekly_backup_dir, is_weekly=is_weekly)

        # Cleanup old backups
        delete_old_files(backup_dir, int(config['retention']['RETENTION_DAYS']))
        delete_old_files(weekly_backup_dir, int(config['retention']['WEEKLY_RETENTION_DAYS']))

        logging.info("Backup process completed successfully.")

    except Exception as e:
        logging.error(f"Critical error: {e}")

if __name__ == "__main__":
    main()
