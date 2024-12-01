# Basic Argument Parsing
import argparse

parser = argparse.ArgumentParser(description="Basic argument parsing example.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args()

print(f"Hello, {args.name}!")
