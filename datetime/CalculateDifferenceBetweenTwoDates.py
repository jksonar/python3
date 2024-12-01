# Calculate the Difference Between Two Dates
from datetime import datetime

date1 = datetime(2024, 11, 27)
date2 = datetime(2024, 12, 1)
difference = date2 - date1
print(f"Difference in days: {difference.days}")
