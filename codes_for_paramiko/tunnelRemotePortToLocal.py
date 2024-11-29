# Tunnel Remote Port to Local
import paramiko
from paramiko import Transport

def port_forwarding(local_port, remote_host, remote_port):
    transport = Transport(("hostname", 22))
    transport.connect(username="user", password="password")
    transport.request_port_forward("", local_port, remote_host, remote_port)
    print(f"Forwarding port {local_port} to {remote_host}:{remote_port}")

port_forwarding(8080, "127.0.0.1", 80)
