# Check Remote Directory Contents
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")

sftp = ssh.open_sftp()
for file in sftp.listdir("."):
    print(file)
sftp.close()
ssh.close()
