# Parse Key-Value Pairs
import argparse

parser = argparse.ArgumentParser(description="Parse key-value pairs.")
parser.add_argument("--keyval", nargs="*", help="Key-value pairs.")
args = parser.parse_args()

if args.keyval:
    parsed = dict(kv.split("=") for kv in args.keyval)
    print(parsed)
