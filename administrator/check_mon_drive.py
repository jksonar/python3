import os

def check_mounts():
    mounts = os.popen("df -h").read()
    print("Mounted Drives:\n", mounts)

check_mounts()
