# Basic Usage
from fabric import Connection

# Connect to a remote host
conn = Connection(host="remote_server", user="username", connect_kwargs={"password": "your_password"})

# Capture Command Output

result = conn.run("uname -a", hide=True)
print(f"Command output: {result.stdout.strip()}")

# Check Command Status
result = conn.run("ls non_existent_file", warn=True)
if result.ok:
    print("Command succeeded")
else:
    print("Command failed")
