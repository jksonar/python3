from fabric import Group

# Define a group of hosts
group = Group(
    "user@192.168.1.10",
    "user@192.168.1.11",
    "user@192.168.1.12",
    connect_kwargs={"password": "password"}
)

# Run a command on all hosts
group.run("uptime")

# Basic Usage
from fabric import Connection

# Connect to a remote host
conn = Connection(host="remote_server", user="username", connect_kwargs={"password": "your_password"})

# Automate System Updates
conn.sudo("apt update && apt upgrade -y")

# Monitor System Resources
result = conn.run("top -b -n 1 | head -5", hide=True)
print(result.stdout)
