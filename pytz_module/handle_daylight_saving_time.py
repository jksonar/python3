from datetime import datetime
import pytz

tz = pytz.timezone('Europe/Paris')
dt = datetime(2024, 3, 31, 1, 30)  # Just before DST change
localized_dt = tz.localize(dt, is_dst=None)  # Auto handle DST
print("Paris Time (with DST adjustment):", localized_dt)
