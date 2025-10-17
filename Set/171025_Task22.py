#find even and odd numbers in a set
#numbers = {10, 15, 22, 33, 40, 57, 68, 71}

numbers = set()
n = 5
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))  
    numbers.add(num)  
   
print("\nNumbers in the set:", numbers)

even_numbers = set()
odd_numbers = set()

for num in numbers:
    if num % 2 == 0:         
        even_numbers.add(num)
    else:
        odd_numbers.add(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
