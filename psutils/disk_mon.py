import psutil

# Get Disk Partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Device: {partition.device}, Mountpoint: {partition.mountpoint}, Filesystem Type: {partition.fstype}")

# Get Disk Usage
disk_usage = psutil.disk_usage('/')
print(f"Total Disk Space: {disk_usage.total // (1024 ** 3)} GB")
print(f"Used Disk Space: {disk_usage.used // (1024 ** 3)} GB")
print(f"Free Disk Space: {disk_usage.free // (1024 ** 3)} GB")

# Get Disk I/O Statistics
disk_io = psutil.disk_io_counters()
print(f"Read Count: {disk_io.read_count}, Write Count: {disk_io.write_count}")
