# 9. Convert Timestamp to Timezone-Aware Datetime
from datetime import datetime
import pytz

timestamp = 1704045600  # Example timestamp
dt = datetime.fromtimestamp(timestamp, pytz.timezone('Europe/Berlin'))
print("Berlin Time from Timestamp:", dt)
