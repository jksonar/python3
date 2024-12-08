import logging
from fabric import Connection

logging.basicConfig(level=logging.INFO)

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})
conn.run("uptime")
