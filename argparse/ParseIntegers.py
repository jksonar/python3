# Parse Integers
import argparse

parser = argparse.ArgumentParser(description="Accept an integer as input.")
parser.add_argument("--count", type=int, help="Number of items.")
args = parser.parse_args()

print(f"Count: {args.count}")
