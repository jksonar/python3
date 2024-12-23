from datetime import datetime
import pytz

local_tz = pytz.timezone('Europe/London')
local_time = local_tz.localize(datetime.now())
utc_time = local_time.astimezone(pytz.utc)

print("Local Time (London):", local_time)
print("UTC Time:", utc_time)
