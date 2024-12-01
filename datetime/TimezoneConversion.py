# Timezone Conversion
from datetime import datetime, timezone, timedelta

utc = timezone.utc
local_tz = timezone(timedelta(hours=5, minutes=30))  # Example: IST
utc_time = datetime.now(utc)
local_time = utc_time.astimezone(local_tz)
print(f"Local time: {local_time}")
