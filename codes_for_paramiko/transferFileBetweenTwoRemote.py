#  Transfer Files Between Two Remote Servers
import paramiko

ssh1 = paramiko.SSHClient()
ssh2 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh1.connect("remote_server1", username="user", password="password")
ssh2.connect("remote_server2", username="user", password="password")

sftp1 = ssh1.open_sftp()
sftp2 = ssh2.open_sftp()

remote_file = "/path/on/server1/file.txt"
transfer_file = "/tmp/temp_file.txt"

# Download from server1 to a local temp location
sftp1.get(remote_file, transfer_file)

# Upload to server2
sftp2.put(transfer_file, "/path/on/server2/file.txt")
print("File transferred between remote servers.")

sftp1.close()
sftp2.close()
ssh1.close()
ssh2.close()
