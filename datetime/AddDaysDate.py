# Add Days to a Date
from datetime import datetime, timedelta

today = datetime.now()
new_date = today + timedelta(days=5)
print(f"Date after 5 days: {new_date}")
