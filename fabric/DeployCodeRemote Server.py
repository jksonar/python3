# Deploy Code to a Remote Server
from fabric import Connection

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})

# Upload the code
conn.put("my_project.zip", "/var/www/my_project.zip")

# Extract the code and restart the server
conn.run("unzip /var/www/my_project.zip -d /var/www/my_project")
conn.sudo("systemctl restart my_app")
