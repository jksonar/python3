# 8. Get UTC Offset for a Timezone
from datetime import datetime
import pytz

tz = pytz.timezone('Australia/Sydney')
dt = datetime.now(tz)
offset = dt.utcoffset()
print("UTC Offset for Sydney:", offset)
