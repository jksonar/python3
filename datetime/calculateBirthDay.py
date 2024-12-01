# Calculate Age from Birth Date
from datetime import datetime

birth_date = datetime(1990, 5, 15)
today = datetime.now()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print(f"Age: {age}")
