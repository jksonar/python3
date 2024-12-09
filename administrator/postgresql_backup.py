import time
from datetime import date
import calendar
import shutil
from subprocess import Popen, PIPE

# find date and pass it to 
my_date = date.today()

to_dayis = calendar.day_name[my_date.weekday()]

# date var for file name 
date_uniq = time.strftime("%Y_%m_%d_%H_%M")

# database name which is present on server
db_name="dedivipu_db1"

# log file for script output \ error
log_name="D:\\dbscript_{}.log".format(date_uniq)

# bin command for pg dump 
db_command="C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump.exe"

# database backup file name 
db_bkp="D:\\dedivipu_db1_{}.sql".format(date_uniq)

db_bkp_weekly="D:\\weekly\\dedivipu_db1_{}.sql".format(date_uniq)

#C:\Program Files\PostgreSQL\14\bin\pg_dump

with open(log_name,'w',encoding='utf-8') as log:
    proc = Popen([db_command, db_name, '-f', db_bkp], stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    log.write(stdout.decode())
    log.write(stderr.decode())
    log.close()
    if to_dayis == "Wednesday":
        shutil.copyfile(db_bkp, db_bkp_weekly)



# This code removes files in the current working directory that were created >= 7 days ago. Run at your own risk.
# need to test 
# import os
# import time

# current_time = time.time()

# for f in os.listdir():
#     creation_time = os.path.getctime(f)
#     if (current_time - creation_time) // (24 * 3600) >= 7:
#         os.unlink(f)  # change with print 
#         print('{} removed'.format(f))

# pg_dump.exe -U postgres -d testdb -f D:\BackupData\import_dump.sql