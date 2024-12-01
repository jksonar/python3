# Generate a List of Dates
from datetime import datetime, timedelta

start_date = datetime(2024, 11, 25)
dates = [start_date + timedelta(days=i) for i in range(7)]
print("Next 7 days:", dates)
