# Combine argparse with Logging
import argparse
import logging

parser = argparse.ArgumentParser(description="Use logging with argparse.")
parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
logging.debug("Debug logging enabled.")
logging.info("Script executed.")
