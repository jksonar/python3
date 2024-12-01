# Handle Password Inputs
import argparse
from getpass import getpass

parser = argparse.ArgumentParser(description="Handle password input securely.")
parser.add_argument("--user", help="Username.")
args = parser.parse_args()

password = getpass("Password: ")
print(f"Username: {args.user}, Password: {password}")
