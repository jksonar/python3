# Execute a Command as a Specific User
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="password")

command = "sudo -u other_user whoami"
stdin, stdout, stderr = ssh.exec_command(command)
stdin.write("password\n")  # Provide password for sudo
stdin.flush()
print(stdout.read().decode())

ssh.close()
