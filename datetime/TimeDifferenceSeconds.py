# Get Time Difference in Seconds
from datetime import datetime

time1 = datetime(2024, 11, 27, 12, 0)
time2 = datetime(2024, 11, 27, 12, 30)
difference = (time2 - time1).seconds
print(f"Difference in seconds: {difference}")
