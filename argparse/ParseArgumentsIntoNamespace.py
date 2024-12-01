# Parse Arguments into a Namespace
import argparse

parser = argparse.ArgumentParser(description="Store arguments in a namespace.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args()

print(vars(args))  # Convert namespace to dictionary
