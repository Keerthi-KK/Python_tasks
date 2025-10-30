#program to subtract 5 days from current date

from datetime import datetime,timedelta

x=datetime.now().date()
print("current date",x)
y=5
z=x-timedelta(days=y)
print("five days before current date:",z)
