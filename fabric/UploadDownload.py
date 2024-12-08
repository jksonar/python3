from fabric import Connection

conn = Connection(host="192.168.1.10", user="user", connect_kwargs={"password": "password"})


# Upload a File
conn.put("local_file.txt", "/remote/path/to/remote_file.txt")
print("File uploaded!")

# Download a File

conn.get("/remote/path/to/remote_file.txt", "local_file.txt")
print("File downloaded!")
