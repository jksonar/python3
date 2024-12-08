# Run Commands on a Remote Machine 
# Basic Command Execution
from fabric import Connection

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})

# Run a command
conn.run("df -h")


# Run Commands as Root
conn.sudo("apt update && apt upgrade -y")
