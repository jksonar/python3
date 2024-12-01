# Restrict Number of Arguments
import argparse

parser = argparse.ArgumentParser(description="Restrict the number of arguments.")
parser.add_argument("--coords", nargs=2, help="Provide exactly two coordinates.")
args = parser.parse_args()

print(f"Coordinates: {args.coords}")
