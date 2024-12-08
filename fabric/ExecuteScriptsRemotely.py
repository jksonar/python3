# Basic Usage
from fabric import Connection

# Connect to a remote host
conn = Connection(host="remote_server", user="username", connect_kwargs={"password": "your_password"})

# Run a Python Script
conn.run("python3 /path/to/script.py")

# Run a Shell Script
conn.run("bash /path/to/script.sh")
