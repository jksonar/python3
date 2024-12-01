# Chain Subcommands
import argparse

parser = argparse.ArgumentParser(description="Chain subcommands example.")
subparsers = parser.add_subparsers(dest="command")

build_parser = subparsers.add_parser("build", help="Build something.")
build_parser.add_argument("--target", help="Target to build.")

deploy_parser = subparsers.add_parser("deploy", help="Deploy something.")
deploy_parser.add_argument("--env", help="Environment to deploy.")

args = parser.parse_args()

if args.command == "build":
    print(f"Building {args.target}.")
elif args.command == "deploy":
    print(f"Deploying to {args.env}.")
