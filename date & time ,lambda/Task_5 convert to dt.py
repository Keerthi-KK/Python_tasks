#to convert a string to date time
from datetime import datetime

date_str="July 1 14 2:43PM"
dt=datetime.strptime(date_str,"%B %d %y %I:%M%p")
print("converted date time is :",dt)
