from datetime import datetime

# now() method is used to get object
# containing current date & time.
now = datetime.now()

# strftime() method used to create a string
# representing the current time.
currentTime = now.strftime("%H:%M:%S")
print("Current Time =", currentTime)
