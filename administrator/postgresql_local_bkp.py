import time
import os
from datetime import date
import calendar
import shutil
from subprocess import Popen, PIPE
from pathlib import Path
from zipfile import ZipFile
# tested script working on local system 

# find date and pass it to 
my_date = date.today()

to_dayis = calendar.day_name[my_date.weekday()]

# date var for file name 
date_uniq = time.strftime("%Y_%m_%d_%H_%M")

# database name which is present on server
db_name="jksonar"

# log file for script output \ error
log_name="D:\\dbscript_{}.log".format(date_uniq)

# bin command for pg dump   D:\iso\pgsql\bin
db_command="d:\\iso\\pgsql\\bin\\pg_dump.exe"

# database backup file name 
db_bkp="D:\\jksonar_{}.sql".format(date_uniq)

db_bkp_weekly="D:\\weekly\\dedivipu_db1_{}.sql".format(date_uniq)

# User Credintials
phost = "192.168.56.145"
port = "5432"
puser = "jay"
os.environ["PGPASSWORD"]="TomAndJ3rry"
current_time = time.time()

File_To_Del = "D:\\DATA\\docker\\multidocker"
File_To_Del_w = "D:\\DATA\\docker\\multidocker"

def creat_zip(bkp_file):
    zip_file_name = '{}.zip'.format(bkp_file)
    zip_file_name_w = '{}.zip'.format(db_bkp_weekly)
    with ZipFile(zip_file_name,'w') as zip:
        zip.write(db_bkp)
        os.unlink(db_bkp)
        if to_dayis == "Wednesday":
            shutil.copyfile(zip_file_name, zip_file_name_w)
        

def main():
    with open(log_name,'w',encoding='utf-8') as log:
        proc = Popen([db_command, "-h", phost, "-p", port, "-U", puser, "-d", db_name, "-f", db_bkp], stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()

        log.write(stdout.decode())
        log.write(stderr.decode())

        for f in os.listdir(File_To_Del):
            creation_time = os.path.getctime(f)
            if (current_time - creation_time) // (24 * 3600) >= 7:
                pathf = Path(f)
                # check if it is file and end with sql.zip then delete it.
                if pathf.is_file() and f.endswith(".sql.zip"):
                    # os.unlink(f)  # change with print
                    log.write('{} is removed from backup\n'.format(f))

        for fw in os.listdir(File_To_Del_w):
            creation_time = os.path.getctime(fw)
            if (current_time - creation_time) // (24 * 3600) >= 20:
                pathfw = Path(fw)
                if pathfw.is_file() and fw.endswith(".sql.zip"):
                    # os.unlink(fw)  # change with print
                    log.write('{} is removed from weekly backup\n'.format(fw))
        log.close()

if __name__=="__main__":
    main()
    creat_zip(db_bkp)