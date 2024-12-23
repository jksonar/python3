import time


# localtime() method used to get the object containing the local time.
t = time.localtime()

# strftime() method used to create a string representing the current time.
currentTime = t.strftime("%H:%M:%S", t)
print(currentTime)