#  Get Remote File Attributes
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
attrs = sftp.stat("/remote_path/remote_file.txt")
print("Size:", attrs.st_size)
print("Permissions:", attrs.st_mode)
print("Modified:", attrs.st_mtime)
sftp.close()
ssh.close()
