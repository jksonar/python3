# Short and Long Options
import argparse

parser = argparse.ArgumentParser(description="Short and long options.")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
args = parser.parse_args()

if args.verbose:
    print("Verbose mode is ON.")
