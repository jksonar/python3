# Provide Help Text
import argparse

parser = argparse.ArgumentParser(description="Add help text for arguments.")
parser.add_argument("--name", help="Your name.")
args = parser.parse_args()
