import socket
import hashlib

PASSWORD = "secure123"  # Set your password here
PASSWORD_HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()  # Hash the password

def start_server(host='0.0.0.0', port=5001, save_path='received_file.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[*] Listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        print(f"[+] Connection from {addr}")

        # Receive and verify hashed password
        received_hash = conn.recv(1024).decode()
        if received_hash != PASSWORD_HASH:
            print("[-] Authentication failed. Closing connection.")
            conn.close()
            return
        conn.send(b"AUTH_SUCCESS")

        # Receive the file
        with open(save_path, 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"[+] File received and saved to {save_path}")
        conn.close()

if __name__ == "__main__":
    start_server()
