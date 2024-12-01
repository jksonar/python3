# Time Difference in Hours and Minutes
from datetime import datetime

start = datetime(2024, 11, 27, 8, 0)
end = datetime(2024, 11, 27, 14, 30)
difference = end - start
hours, remainder = divmod(difference.seconds, 3600)
minutes = remainder // 60
print(f"Difference: {hours} hours and {minutes} minutes")
