# Positional Arguments
import argparse

parser = argparse.ArgumentParser(description="Demonstrate positional arguments.")
parser.add_argument("filename", help="The name of the file to process.")
args = parser.parse_args()

print(f"Processing file: {args.filename}")
