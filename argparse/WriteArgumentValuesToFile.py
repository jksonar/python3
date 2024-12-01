# Write Argument Values to a File
import argparse

parser = argparse.ArgumentParser(description="Write arguments to a file.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args()

with open("output.txt", "w") as f:
    f.write(f"Name: {args.name}\n")
print("Arguments saved to output.txt.")
