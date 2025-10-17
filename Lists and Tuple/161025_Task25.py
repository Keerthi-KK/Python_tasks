#Count Odd Numbers - Count how many odd numbers are in (1, 2, 3, 4, 5, 6, 7)

t = (1, 2, 3, 4, 5, 6, 7)
count = 0
for i in t:
    if i % 2 != 0:
        count += 1
print("Count of odd numbers:", count)
