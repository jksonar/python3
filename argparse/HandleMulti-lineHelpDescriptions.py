# Handle Multi-line Help Descriptions
import argparse

parser = argparse.ArgumentParser(
    description="""This tool demonstrates how to handle
    multi-line descriptions in argparse.""",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument("--example", help="An example argument.")
args = parser.parse_args()
