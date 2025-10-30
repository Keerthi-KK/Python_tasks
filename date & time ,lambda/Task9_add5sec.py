#program to add 5seconds to current time
from datetime import datetime,timedelta

#time1=datetime.strptime("21:33:0","%H:%M:%S")
time1=datetime.now()
print("Current time:",time1)
new_time=time1+timedelta(seconds=5)
print("After adding 5 seconds:",new_time)
