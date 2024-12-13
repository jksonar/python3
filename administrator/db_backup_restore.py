# 1. read ini file db_backup.ini
# 2. take backup of MySQL , PostgreSQL databases backup
# 3. take daly backup or weekly backup
# 4. copy backup files to remote server
# 5. remove old backup files base on retention from remote and local

import configparser
import os
import subprocess

config = configparser.ConfigParser()
FilePath = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
iniFileName = os.path.join(FilePath, 'db_backup.ini')
config.read(iniFileName)

host = config['DEFAULT']['host']
port = config['DEFAULT']['port']
user = config['DEFAULT']['user']
os.environ["PGPASSWORD"] = config['DEFAULT']['password']
database = config['DEFAULT']['database']
backup_folder_path = config['DEFAULT']['backup_folder_path']

if 'postgres' == config['DEFAULT']['db_engin']:
    result = subprocess.run(["pg_dump", "-h", host, "--user", user, "-d", database, "-f", os.path.join(backup_folder_path,"emp.sql")], capture_output=True, text=True)

# if condition for mysql command
if 'mysql' == config['DEFAULT']['db_engin']:
    pass

#if condition for copy backup to remote using ssh 
if config['DEFAULT']['copy_remote_ssh']:
    pass