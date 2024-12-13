# 1. read ini file db_backup.ini
# 2. take backup of MySQL , PostgreSQL databases backup
# 3. take daly backup or weekly backup
# 4. copy backup files to remote server
# 5. remove old backup files base on retention from remote and local

import configparser

config = configparser.ConfigParser()
config.read('D:\\DATA\\python3\\administrator\\db_backup.ini')


