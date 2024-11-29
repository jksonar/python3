# Manage Remote Users
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="admin", password="password")
stdin, stdout, stderr = ssh.exec_command("sudo useradd new_user")
print("New user added.")
ssh.close()
