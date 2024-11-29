# Change Remote File Permissions
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
sftp.chmod("/remote_path/remote_file.txt", 0o644)
print("Permissions changed.")
sftp.close()
ssh.close()
