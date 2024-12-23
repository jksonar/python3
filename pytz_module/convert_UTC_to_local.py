from datetime import datetime
import pytz

utc_time = datetime.now(pytz.utc)
local_tz = pytz.timezone('America/New_York')
local_time = utc_time.astimezone(local_tz)

print("UTC Time:", utc_time)
print("Local Time (New York):", local_time)
