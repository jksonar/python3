import socket

def check_ports(host="127.0.0.1", ports=[22, 80, 443]):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
        s.close()

check_ports()
