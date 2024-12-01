# Multiple Mutually Exclusive Groups
import argparse

parser = argparse.ArgumentParser(description="Handle multiple exclusive groups.")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("--add", action="store_true", help="Add something.")
group1.add_argument("--delete", action="store_true", help="Delete something.")

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("--enable", action="store_true", help="Enable feature.")
group2.add_argument("--disable", action="store_true", help="Disable feature.")

args = parser.parse_args()

if args.add:
    print("Adding.")
if args.delete:
    print("Deleting.")
if args.enable:
    print("Enabling feature.")
if args.disable:
    print("Disabling feature.")
