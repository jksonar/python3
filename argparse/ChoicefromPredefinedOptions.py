# Choice from Predefined Options
import argparse

parser = argparse.ArgumentParser(description="Select an option.")
parser.add_argument("--color", choices=["red", "green", "blue"], help="Choose a color.")
args = parser.parse_args()

print(f"Color chosen: {args.color}")
