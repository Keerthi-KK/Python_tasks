#multiplication of items in a dictionary

d1={}
n=int(input("Enter the count of dictionary 1:"))
for i in range(n):
    key=input("Enter key value")
    value=int(input("Enter value"))
    d1[key]=value

print("Given dict 1 is:",d1)
result=1
for value in d1.values():
    result*=value

print("product of values is ",result)
