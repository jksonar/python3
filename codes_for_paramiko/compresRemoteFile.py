# Compress Remote Files
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("tar -czvf archive.tar.gz /path/to/directory")
print("Compression completed.")
ssh.close()
