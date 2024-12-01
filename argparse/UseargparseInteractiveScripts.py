# Use argparse in Interactive Scripts
import argparse

parser = argparse.ArgumentParser(description="Interactive argparse example.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args()

if not args.name:
    args.name = input("Enter your name: ")

print(f"Hello, {args.name}!")
