# Get ISO 8601 Format Date
from datetime import datetime

now = datetime.now()
iso_date = now.isoformat()
print(f"ISO 8601 date: {iso_date}")
