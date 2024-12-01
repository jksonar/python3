# Download Files Using SFTP
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")

sftp = ssh.open_sftp()
sftp.get("remote_file.txt", "local_file.txt")
print("File downloaded.")
sftp.close()
ssh.close()
