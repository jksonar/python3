# Parse Arguments from a List 
import argparse

parser = argparse.ArgumentParser(description="Parse arguments from a list.")
parser.add_argument("--test", help="Test argument.")
args = parser.parse_args(["--test", "value"])  # Simulate command-line input
print(f"Test argument: {args.test}")
