# Parse Date Range
import argparse
from datetime import datetime

def valid_date(value):
    return datetime.strptime(value, "%Y-%m-%d")

parser = argparse.ArgumentParser(description="Parse date range.")
parser.add_argument("--start", type=valid_date, help="Start date (YYYY-MM-DD).")
parser.add_argument("--end", type=valid_date, help="End date (YYYY-MM-DD).")
args = parser.parse_args()

print(f"Date range: {args.start} to {args.end}")
