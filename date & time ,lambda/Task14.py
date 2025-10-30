#Convert difference of two dates into days, hours, minutes, and seconds
import datetime

datetime1 = datetime.datetime(2020, 5, 10, 8, 0, 0)
datetime2 = datetime.datetime(2020, 5, 12, 10, 30, 15)

diff = datetime2 - datetime1
days = diff.days
seconds = diff.seconds

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"Difference: {days} days, {hours} hours, {minutes} minutes, {secs} seconds")
