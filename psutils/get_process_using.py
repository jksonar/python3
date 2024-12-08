# Get Processes Using High CPU
import psutil


for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    if process.info['cpu_percent'] > 50:  # Threshold
        print(f"High CPU Usage - PID: {process.info['pid']}, Name: {process.info['name']}, CPU: {process.info['cpu_percent']}%")
