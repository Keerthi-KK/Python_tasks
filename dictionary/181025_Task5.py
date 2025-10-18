#sum of values in dictionary

d1={}
n=int(input("Enter the count of dictionary 1:"))
for i in range(n):
    key=input("Enter key value")
    value=int(input("Enter value"))
    d1[key]=value

print("Given dict 1 is:",d1)

print("Sum of all values is ",sum(d1.values()))
