numbers=[]

for i in range(5):
    num=int(input("enter a number:"))
    numbers.append(num)
print("numbers entered",numbers)
largest=max(numbers)
print("Largest number is :",largest)
