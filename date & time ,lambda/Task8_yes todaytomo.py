#program to print yesterday ,today and tomorrow

from datetime import datetime,timedelta,date

today=date.today()
print("Today's date:",today)
yesterday=today-timedelta(days=1)
print("Yesterday's date:",yesterday)
tomorrow =today+timedelta(days=1)
print("Tomorrow's date:",tomorrow)
