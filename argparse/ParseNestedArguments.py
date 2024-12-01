# Parse Nested Arguments
import argparse

parser = argparse.ArgumentParser(description="Parse nested arguments.")
parser.add_argument("--user", nargs=2, metavar=("USERNAME", "PASSWORD"), help="Provide username and password.")
args = parser.parse_args()

print(f"Username: {args.user[0]}, Password: {args.user[1]}")
