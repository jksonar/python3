from datetime import datetime
import pytz

# Define the timezone for India
tz_india = pytz.timezone('Asia/Kolkata')

# Get the current time in India time zone
datetime_india = datetime.now(tz_india)
print("India Time:", datetime_india.strftime("%H:%M:%S"))