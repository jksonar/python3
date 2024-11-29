# Decompress Remote Files
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("tar -xzvf archive.tar.gz -C /destination")
print("Decompression completed.")
ssh.close()
