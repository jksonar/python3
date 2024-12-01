# Parse Floats
import argparse

parser = argparse.ArgumentParser(description="Accept a float as input.")
parser.add_argument("--price", type=float, help="Price of the item.")
args = parser.parse_args()

print(f"Price: {args.price}")
