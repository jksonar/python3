# This example uses Paramiko to SSH into the remote host and check if a directory exists.
import paramiko

def check_remote_directory(host, port, username, password, directory_path):
    """Check if a directory exists on a remote server using Paramiko."""
    try:
        # Create an SSH client instance
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        client.connect(hostname=host, port=port, username=username, password=password)

        # Command to check if the directory exists
        command = f"if [ -d '{directory_path}' ]; then echo 'exists'; else echo 'not exists'; fi"

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()

        # Print the result
        if output == "exists":
            print(f"The directory '{directory_path}' exists on {host}.")
        else:
            print(f"The directory '{directory_path}' does NOT exist on {host}.")

        # Close the connection
        client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Remote host details
    remote_host = "192.168.56.101"
    remote_port = 22
    username = "user"
    password = "password"
    directory_path = "/home/user/test_directory"

    # Check the directory
    check_remote_directory(remote_host, remote_port, username, password, directory_path)
