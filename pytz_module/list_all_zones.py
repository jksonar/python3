# 2. List All Available Timezones
import pytz

timezones = pytz.all_timezones
for tz in timezones[:10]:  # Print first 10 timezones
    print(tz)
