# Round Time to Nearest Minute
from datetime import datetime

now = datetime.now()
rounded = now.replace(second=0, microsecond=0)
print(f"Rounded time: {rounded}")
