from fabric import Connection

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})

conn.run("export MY_VAR=value && echo $MY_VAR")
