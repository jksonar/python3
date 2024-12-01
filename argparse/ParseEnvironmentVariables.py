# Parse Environment Variables
import argparse
import os

parser = argparse.ArgumentParser(description="Use environment variables.")
parser.add_argument(
    "--config",
    default=os.getenv("APP_CONFIG", "default-config.json"),
    help="Path to the config file (can be set via APP_CONFIG env var).",
)
args = parser.parse_args()

print(f"Config path: {args.config}")
