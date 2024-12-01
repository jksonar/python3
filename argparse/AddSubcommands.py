# Add Subcommands
import argparse

parser = argparse.ArgumentParser(description="Support multiple subcommands.")
subparsers = parser.add_subparsers(dest="command", help="Subcommand to execute.")

create_parser = subparsers.add_parser("create", help="Create something.")
delete_parser = subparsers.add_parser("delete", help="Delete something.")

args = parser.parse_args()

if args.command == "create":
    print("Create command executed.")
elif args.command == "delete":
    print("Delete command executed.")
