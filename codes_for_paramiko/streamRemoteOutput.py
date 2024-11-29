# Stream Remote Command Output
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("tail -f /var/log/syslog")
for line in iter(stdout.readline, ""):
    print(line, end="")
ssh.close()
