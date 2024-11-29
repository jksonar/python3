# Rename a Remote File
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
sftp.rename("/remote_path/old_name.txt", "/remote_path/new_name.txt")
print("File renamed.")
sftp.close()
ssh.close()
