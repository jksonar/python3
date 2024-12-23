import os

def list_cron_jobs():
    cron_jobs = os.popen("crontab -l").read()
    print("Crontab Jobs:\n", cron_jobs)

list_cron_jobs()
