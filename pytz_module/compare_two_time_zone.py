# 6. Time Difference Between Two Timezones
from datetime import datetime
import pytz

tz1 = pytz.timezone('America/New_York')
tz2 = pytz.timezone('Asia/Tokyo')

time_now = datetime.now(pytz.utc)
ny_time = time_now.astimezone(tz1)
tokyo_time = time_now.astimezone(tz2)

time_diff = tokyo_time - ny_time
print("Time Difference (Tokyo - New York):", time_diff)
