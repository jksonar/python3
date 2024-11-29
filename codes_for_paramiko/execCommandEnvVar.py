# Execute a Command with Environment Variables
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
command = "export MY_VAR='Hello' && echo $MY_VAR"
stdin, stdout, stderr = ssh.exec_command(command)
print(stdout.read().decode())
ssh.close()
