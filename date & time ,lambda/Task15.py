#Calculate age in years
import datetime

birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()

today = datetime.date.today()

age = today.year - birthdate.year

if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

print("Your age is:", age, "years")

