# Boolean Flag
import argparse

parser = argparse.ArgumentParser(description="Toggle a feature.")
parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
args = parser.parse_args()

if args.debug:
    print("Debug mode enabled.")
else:
    print("Debug mode disabled.")
