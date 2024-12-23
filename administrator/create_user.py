import subprocess

def create_user(username):
    try:
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create user.")

create_user("newadmin")
