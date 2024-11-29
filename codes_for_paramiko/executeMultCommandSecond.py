# Execute Multiple Commands in One Session
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")

commands = ["echo 'Hello, World!'", "ls -l", "pwd"]
for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(f"Output of '{command}':")
    print(stdout.read().decode())

ssh.close()
