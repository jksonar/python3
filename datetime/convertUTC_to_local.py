# Convert UTC to Local Time
from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)
local_time = utc_time.astimezone()
print(f"Local time: {local_time}")
