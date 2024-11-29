# Schedule Cron Jobs on Remote Server
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command('(crontab -l ; echo "0 2 * * * /path/to/script.sh") | crontab -')
print("Cron job scheduled.")
ssh.close()
