# Fabric simplifies SSH operations by providing a higher-level API over Paramiko.
from fabric import Connection

def check_remote_directory_with_fabric(host, user, password, directory_path):
    """Check if a directory exists on a remote server using Fabric."""
    try:
        # Connect to the remote host
        conn = Connection(host=host, user=user, connect_kwargs={"password": password})

        # Command to check the directory
        result = conn.run(f"if [ -d '{directory_path}' ]; then echo 'exists'; else echo 'not exists'; fi", hide=True)

        # Check the output
        if "exists" in result.stdout.strip():
            print(f"The directory '{directory_path}' exists on {host}.")
        else:
            print(f"The directory '{directory_path}' does NOT exist on {host}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Remote host details
    remote_host = "192.168.56.101"
    username = "user"
    password = "password"
    directory_path = "/home/user/test_directory"

    # Check the directory using Fabric
    check_remote_directory_with_fabric(remote_host, username, password, directory_path)
