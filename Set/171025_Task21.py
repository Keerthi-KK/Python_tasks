#perfect number


numbers = set()

n = int(input("How many numbers do you want to enter? "))


for k in range(n):
    num = int(input("Enter a number: "))
    numbers.add(num)
print("The numbers in set are :",numbers)

perfect_numbers = set()

for num in numbers:
    if num < 2:
        continue
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        perfect_numbers.add(num)

print("Perfect numbers in the set:", perfect_numbers)
