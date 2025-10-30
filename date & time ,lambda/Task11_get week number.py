#get week number

from datetime import datetime,date
year=int(input("Enter year"))
month =int(input("enter month"))
day=int(input ("Enter day"))
sample_date=date(year,month,day)
print("Week number:",sample_date.strftime("%U"))
