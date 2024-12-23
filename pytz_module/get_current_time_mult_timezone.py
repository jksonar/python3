# 10. Get Current Time in Multiple Timezones
from datetime import datetime
import pytz

zones = ['America/Los_Angeles', 'Asia/Tokyo', 'Asia/Kolkata', 'Europe/London']

for zone in zones:
    tz = pytz.timezone(zone)
    print(f"Current time in {zone}: {datetime.now(tz)}")
