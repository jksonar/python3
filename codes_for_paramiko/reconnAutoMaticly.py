# Reconnect Automatically on Failure
import paramiko
from time import sleep

def connect_ssh():
    while True:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("hostname", username="user", password="password")
            print("Connected.")
            return ssh
        except paramiko.SSHException as e:
            print("Connection failed. Retrying in 5 seconds.")
            sleep(5)

ssh = connect_ssh()
ssh.close()
