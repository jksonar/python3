import os

def system_uptime():
    uptime = os.popen("uptime -p").read()
    print(f"System Uptime: {uptime}")

system_uptime()
