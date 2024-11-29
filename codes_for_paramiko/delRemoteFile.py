# Delete a Remote Directory
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("rm -rf /path/to/directory")
print("Directory deleted.")
ssh.close()
