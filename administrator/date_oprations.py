# Find yesterday’s, today’s and tomorrow’s date

# Python program to find yesterday,
# today and tomorrow


# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta


# Get today's date
presentday = datetime.now() # or presentday = datetime.today()

# Get Yesterday
yesterday = presentday - timedelta(1)

# Get Tomorrow
tomorrow = presentday + timedelta(1)


# strftime() is to format date according to
# the need by converting them to string
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))

# Find yesterday’s, today’s and tomorrow’s date Using calendar method
import calendar
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday = ", calendar.day_name[yesterday.weekday()], yesterday.strftime('%d-%m-%Y'))
print("Today = ", calendar.day_name[today.weekday()], today.strftime('%d-%m-%Y'))
print("Tomorrow = ", calendar.day_name[tomorrow.weekday()], tomorrow.strftime('%d-%m-%Y'))
