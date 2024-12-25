import socket
import hashlib
import os

PASSWORD = "secure123"  # Use the same password as the server
PASSWORD_HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()  # Hash the password

def send_file(host, port, file_path):
    if not os.path.exists(file_path):
        print("[-] File not found!")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("[+] Connected to server")

        # Send hashed password for authentication
        client_socket.send(PASSWORD_HASH.encode())
        response = client_socket.recv(1024).decode()

        if response != "AUTH_SUCCESS":
            print("[-] Authentication failed. Exiting.")
            return

        # Send the file
        with open(file_path, 'rb') as f:
            client_socket.sendfile(f)
        print("[+] File sent successfully")

if __name__ == "__main__":
    server_ip = input("Enter server IP: ")
    file_to_send = input("Enter path to the file to send: ")
    send_file(server_ip, 5001, file_to_send)
