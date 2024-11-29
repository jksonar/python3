# Check if a Remote File Exists
import paramiko

def file_exists(sftp, path):
    try:
        sftp.stat(path)
        return True
    except FileNotFoundError:
        return False

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
sftp = ssh.open_sftp()
print(file_exists(sftp, "/remote_path/remote_file.txt"))
sftp.close()
ssh.close()
