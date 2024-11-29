# Create a Remote Directory
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
sftp.mkdir("/remote_path/new_directory")
print("Directory created.")
sftp.close()
ssh.close()
