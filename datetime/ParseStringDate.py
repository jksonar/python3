# Parse String to Date
from datetime import datetime

date_string = "2024-11-27"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")
