# Parse Date and Time Arguments
import argparse
from datetime import datetime

def valid_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid date (format: YYYY-MM-DD).")

parser = argparse.ArgumentParser(description="Parse date arguments.")
parser.add_argument("--date", type=valid_date, help="Specify a date (format: YYYY-MM-DD).")
args = parser.parse_args()

print(f"Date: {args.date}")
