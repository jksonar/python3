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

config = configparser.ConfigParser()
FilePath = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
iniFileName = os.path.join(FilePath, 'db_backup.ini')
config.read(iniFileName)

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

if 'postgres' == config['DEFAULT']['DB_ENGIN']:
    os.environ["PGPASSWORD"] = config['DEFAULT']['PASSWORD']
    result = Popen(["pg_dump", "-h", HOST, "-U", USER, "-d", DATABASE, "-f", DATABASE_FILE_NAME],stdout=PIPE, stderr=PIPE)
    stdout, stderr = result.communicate()

# if condition for mysql command
if 'mysql' == config['DEFAULT']['DB_ENGIN']:
    pass

#if condition for copy backup to remote using ssh 
if config['DEFAULT']['copy_remote_ssh']:
    pass