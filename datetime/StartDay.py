# Get the Start of the Day
from datetime import datetime

today = datetime.now()
start_of_day = datetime(today.year, today.month, today.day)
print(f"Start of today: {start_of_day}")
