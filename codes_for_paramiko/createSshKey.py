# Create and Manage SSH Keys on Remote
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''")
print("SSH key generated on remote.")
ssh.close()
