# Get Disk Usage
import shutil
usage = shutil.disk_usage("/")
print(f"Total: {usage.total // (1024**3)} GB")
print(f"Used: {usage.used // (1024**3)} GB")
print(f"Free: {usage.free // (1024**3)} GB")
