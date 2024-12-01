# Allow Argument Files
import argparse

parser = argparse.ArgumentParser(description="Read arguments from a file.")
parser.add_argument("--file", type=argparse.FileType("r"), help="File containing arguments.")
args = parser.parse_args()

if args.file:
    print(f"File content: {args.file.read()}")
