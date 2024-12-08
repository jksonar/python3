# Basic Usage
from fabric import Connection

# Connect to a remote host
conn = Connection(host="remote_server", user="username", connect_kwargs={"password": "your_password"})

# Run a command
result = conn.run("uname -a", hide=True)
print(result.stdout.strip())
