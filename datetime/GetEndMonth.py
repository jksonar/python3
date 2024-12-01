# Get the End of the Month
from datetime import datetime
from calendar import monthrange

today = datetime.now()
end_of_month = today.replace(day=monthrange(today.year, today.month)[1])
print(f"End of month: {end_of_month}")
