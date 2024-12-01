# Calculate Next Monday
from datetime import datetime, timedelta

today = datetime.now()
days_until_monday = (7 - today.weekday()) % 7
next_monday = today + timedelta(days=days_until_monday)
print(f"Next Monday: {next_monday}")
