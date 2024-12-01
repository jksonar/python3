# Format Date as String
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
print(f"Formatted date: {formatted_date}")
