# Custom Formatter for Help Messages
import argparse

class CustomHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        super().add_usage(usage, actions, groups, prefix="Custom Usage: ")

parser = argparse.ArgumentParser(
    description="Custom help formatter example.",
    formatter_class=CustomHelpFormatter,
)
parser.add_argument("--example", help="An example argument.")
args = parser.parse_args()
