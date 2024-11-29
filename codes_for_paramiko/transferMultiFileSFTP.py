# Transfer Multiple Files via SFTP
import paramiko
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()

local_dir = "local_folder"
remote_dir = "/remote_folder"

for file in os.listdir(local_dir):
    local_file = os.path.join(local_dir, file)
    remote_file = os.path.join(remote_dir, file)
    sftp.put(local_file, remote_file)
    print(f"Uploaded {file}")

sftp.close()
ssh.close()
