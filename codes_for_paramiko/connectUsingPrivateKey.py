# Connect Using a Private Key 
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("path/to/private_key.pem")
ssh.connect("hostname", username="user", pkey=key)
print("Connected using private key.")
ssh.close()
