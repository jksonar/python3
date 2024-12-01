# Parse from a Configuration File
import argparse

parser = argparse.ArgumentParser(description="Read arguments from a file.")
parser.add_argument("--config", type=argparse.FileType("r"), help="Config file to read.")
args = parser.parse_args()

if args.config:
    print(f"Config contents:\n{args.config.read()}")
