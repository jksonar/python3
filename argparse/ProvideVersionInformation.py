# Provide Version Information
import argparse

parser = argparse.ArgumentParser(description="Provide version info.")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
args = parser.parse_args()
