# Parse Configuration Paths
import argparse

parser = argparse.ArgumentParser(description="Parse configuration paths.")
parser.add_argument("--config", help="Path to the config file.", required=True)
args = parser.parse_args()

print(f"Using config at: {args.config}")
