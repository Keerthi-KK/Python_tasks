#to determine whether a given year is leap year or not
year=int(input("Enter any year"))
if (year % 4==0 and year % 100!=0)or (year%400==0):
    print("leap year")
else:
    print("not leap year")
