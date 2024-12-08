# Run Commands on a Local Machine
from fabric import Connection

# Create a connection to the local machine
conn = Connection("localhost")

# Run a command locally
conn.run("ls -l")
