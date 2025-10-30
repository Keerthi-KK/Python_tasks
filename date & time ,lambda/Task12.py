#Add years to given date
from datetime import date
def addYears(d,years):
    try :
        return d.replace(year=d.year+years)
    except ValueError:
        return d.replace(month=2,day=28,year=d.year+years)
print(addYears(date(2015,1,1),-1))
print(addYears(date(2015,1,1),0))
print(addYears(date(2015,1,1),2))
print(addYears(date(2000,2,29),1))
