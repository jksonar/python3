import os
statvfs = os.statvfs("/")
total_space = statvfs.f_frsize * statvfs.f_blocks  # Total space
free_space = statvfs.f_frsize * statvfs.f_bfree  # Free space
used_space = total_space - free_space  # Used space

print(f"Total Space: {total_space // (1024**3)} GB")
print(f"Free Space: {free_space // (1024**3)} GB")
print(f"Used Space: {used_space // (1024**3)} GB")

# Check Disk Usage (Alert if Full)
import shutil

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100

    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    print(f"Disk Usage: {percent_used:.2f}%")

    if percent_used > 80:
        print("Warning: Disk usage is above 80%")

check_disk_usage()
