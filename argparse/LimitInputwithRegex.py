# Limit Input with Regex
import argparse
import re

def validate_email(value):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(pattern, value):
        raise argparse.ArgumentTypeError(f"{value} is not a valid email.")
    return value

parser = argparse.ArgumentParser(description="Validate email format.")
parser.add_argument("--email", type=validate_email, help="Provide an email address.")
args = parser.parse_args()

print(f"Valid email: {args.email}")
