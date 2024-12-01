# Get UTC Time
from datetime import datetime, timezone

utc_time = datetime.now(timezone.utc)
print(f"Current UTC time: {utc_time}")
