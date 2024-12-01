# Suppress Help Message
import argparse

parser = argparse.ArgumentParser(description="Suppress help message.", add_help=False)
args = parser.parse_args()
