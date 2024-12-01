# Subtract Days from a Date
from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)
print(f"Date 5 days ago: {new_date}")
