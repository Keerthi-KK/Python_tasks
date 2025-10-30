#convert a string to datetime
from datetime import datetime

date_str="July 1 14 2:34PM"
dt=datetime.strptime(date_str,"%B %d %y %I:%M%p")
print("converted date time is :",dt)
