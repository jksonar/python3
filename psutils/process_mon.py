import psutil

# Get a List of All Processes
for process in psutil.process_iter(['pid', 'name', 'username']):
    print(process.info)

# Kill a Process by PID
pid_to_kill = 1234  # Replace with the actual PID
try:
    process = psutil.Process(pid_to_kill)
    process.terminate()
    print(f"Process {pid_to_kill} terminated.")
except psutil.NoSuchProcess:
    print(f"No process with PID {pid_to_kill} found.")

# Get Detailed Info of a Process
pid = 1234  # Replace with the actual PID
try:
    process = psutil.Process(pid)
    print(f"Name: {process.name()}, Status: {process.status()}, Memory Info: {process.memory_info()}")
except psutil.NoSuchProcess:
    print(f"Process with PID {pid} does not exist.")
