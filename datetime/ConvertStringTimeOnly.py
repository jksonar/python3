# Convert String to Time Only
from datetime import datetime

time_string = "14:30:00"
parsed_time = datetime.strptime(time_string, "%H:%M:%S").time()
print(f"Parsed time: {parsed_time}")
