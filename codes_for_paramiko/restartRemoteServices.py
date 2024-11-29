# Restart Remote Services
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="admin", password="password")
stdin, stdout, stderr = ssh.exec_command("sudo systemctl restart nginx")
print("Service restarted.")
ssh.close()
