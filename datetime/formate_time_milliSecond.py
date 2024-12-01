# Format Time with Milliseconds
from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%H:%M:%S.%f")
print(f"Current time with milliseconds: {formatted_time}")
