# Get Battery Info
import psutil

battery = psutil.sensors_battery()
if battery:
    print(f"Battery Percentage: {battery.percent}%")
    print(f"Plugged In: {'Yes' if battery.power_plugged else 'No'}")
else:
    print("Battery information not available.")


# Error Handling in psutil
try:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
except Exception as e:
    print(f"An error occurred: {e}")
