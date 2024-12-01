# Optional Arguments with Default Values
import argparse

parser = argparse.ArgumentParser(description="Optional argument with default value.")
parser.add_argument("--verbosity", default="INFO", help="Set verbosity level (default: INFO).")
args = parser.parse_args()

print(f"Verbosity set to: {args.verbosity}")
