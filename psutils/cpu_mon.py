import psutil

# Get the current CPU utilization as a percentage
cpu_usage = psutil.cpu_percent(interval=1)  # 1-second interval
print(f"CPU Usage: {cpu_usage}%")

# Get CPU Times
# Get detailed CPU times
cpu_times = psutil.cpu_times()
print(f"User Time: {cpu_times.user}, System Time: {cpu_times.system}")

# Get Per-Core Usage
# Get CPU usage for each core
core_usage = psutil.cpu_percent(interval=1, percpu=True)
print(f"Per-Core Usage: {core_usage}")
