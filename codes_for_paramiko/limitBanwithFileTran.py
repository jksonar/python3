#  Limit Bandwidth for File Transfers
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("df -h")
print(stdout.read().decode())
ssh.close()
