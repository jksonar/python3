# Monitor Remote Directory for Changes
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
watched_dir = "/remote_path"
before = set(sftp.listdir(watched_dir))

while True:
    after = set(sftp.listdir(watched_dir))
    added = after - before
    removed = before - after
    if added:
        print("Added:", added)
    if removed:
        print("Removed:", removed)
    before = after
sftp.close()
ssh.close()
