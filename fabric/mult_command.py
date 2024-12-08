from fabric import Connection

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})

with conn:
    conn.run("cd /path/to/dir && ls -l")
    conn.run("pwd")
