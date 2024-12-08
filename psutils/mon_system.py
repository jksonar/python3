# Monitor System Resources Continuously
import time
import psutil

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")
    time.sleep(5)  # Update every 5 seconds
