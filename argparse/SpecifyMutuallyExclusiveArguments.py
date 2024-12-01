# Specify Mutually Exclusive Arguments
import argparse

parser = argparse.ArgumentParser(description="Use mutually exclusive arguments.")
group = parser.add_mutually_exclusive_group()
group.add_argument("--add", action="store_true", help="Add operation.")
group.add_argument("--delete", action="store_true", help="Delete operation.")
args = parser.parse_args()

if args.add:
    print("Adding.")
elif args.delete:
    print("Deleting.")
