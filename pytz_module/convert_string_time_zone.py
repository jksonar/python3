# 7. Convert String to Timezone-Aware Datetime
from datetime import datetime
import pytz

time_string = "2024-12-01 14:30:00"
fmt = "%Y-%m-%d %H:%M:%S"

naive_dt = datetime.strptime(time_string, fmt)
local_dt = pytz.timezone('Asia/Singapore').localize(naive_dt)
print("Timezone Aware Datetime:", local_dt)
