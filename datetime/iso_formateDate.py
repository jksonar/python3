# Parse ISO Format Date
from datetime import datetime

iso_date = "2024-11-27T10:15:30"
parsed_date = datetime.fromisoformat(iso_date)
print(f"Parsed ISO date: {parsed_date}")
