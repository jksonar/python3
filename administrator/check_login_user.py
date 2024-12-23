# Check Logged-in Users
import os

def logged_in_users():
    users = os.popen("who").read()
    print("Logged in users:\n", users)

logged_in_users()
