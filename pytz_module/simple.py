# 1. Basic Example – Get Current Time in Specific Timezone
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata')
time_now = datetime.now(tz)
print("Current time in Kolkata:", time_now)
