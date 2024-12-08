import psutil

# Get Boot Time
from datetime import datetime

boot_time = psutil.boot_time()
boot_time_formatted = datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
print(f"System Boot Time: {boot_time_formatted}")

# Get Logged-In Users
users = psutil.users()
for user in users:
    print(f"User: {user.name}, Terminal: {user.terminal}, Host: {user.host}, Started: {user.started}")
