# Validate Integers Within a Range
import argparse

def check_range(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 10:
        raise argparse.ArgumentTypeError(f"{value} is not in the range 1–10.")
    return ivalue

parser = argparse.ArgumentParser(description="Validate integer input.")
parser.add_argument("--number", type=check_range, help="A number between 1 and 10.")
args = parser.parse_args()

print(f"Number: {args.number}")
