# Measure Network Latency to Server
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("ping -c 4 google.com")
print(stdout.read().decode())
ssh.close()
