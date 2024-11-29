# Upload a File via SFTP
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
sftp.put("local_file.txt", "/remote_path/remote_file.txt")
print("File uploaded.")
sftp.close()
ssh.close()
