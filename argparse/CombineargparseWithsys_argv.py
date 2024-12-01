# Combine argparse with sys.argv
import argparse
import sys

parser = argparse.ArgumentParser(description="Combine argparse with sys.argv.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args(sys.argv[1:])

print(f"Name: {args.name}")
