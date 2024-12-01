# Required Arguments
import argparse

parser = argparse.ArgumentParser(description="Make an argument required.")
parser.add_argument("--user", required=True, help="Specify the username.")
args = parser.parse_args()

print(f"Username: {args.user}")
