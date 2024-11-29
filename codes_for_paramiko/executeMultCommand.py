# Execute Multiple Commands in One SSH Session
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
channel = ssh.invoke_shell()

commands = ["cd /path", "ls -l", "pwd"]
for command in commands:
    channel.send(command + "\n")

while channel.recv_ready():
    output = channel.recv(1024).decode()
    print(output)

ssh.close()
