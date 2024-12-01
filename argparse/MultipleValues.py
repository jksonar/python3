# Multiple Values
import argparse

parser = argparse.ArgumentParser(description="Accept multiple values.")
parser.add_argument("--values", nargs="+", help="A list of values.")
args = parser.parse_args()

print(f"Values: {args.values}")
