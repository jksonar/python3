# Convert Timestamp to Date
from datetime import datetime

timestamp = 1698425600  # Example UNIX timestamp
date = datetime.fromtimestamp(timestamp)
print(f"Date from timestamp: {date}")
