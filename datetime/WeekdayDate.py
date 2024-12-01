# Get the Weekday of a Date
from datetime import datetime

today = datetime.now()
weekday = today.strftime("%A")  # Full weekday name
print(f"Today is: {weekday}")
