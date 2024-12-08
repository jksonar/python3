# Use SSH Keys
# Avoid using passwords directly in your script; use SSH keys instead.

from fabric import Connection

# Connect to a remote host
conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"key_filename": "/path/to/private_key"})
