#merge two python dictionaries

d1={}
n=int(input("Enter the count of dictionary 1:"))
for i in range(n):
    key=input("Enter key value")
    value=input("Enter value")
    d1[key]=value

print("Given dict 1 is:",d1)

d2={}
n2=int(input("Enter the count of dictionary 2:"))
for j in range(n2):
    key=input("Enter key value")
    value=input("Enter value")
    d2[key]=value

print("Given dict 2 is:",d2)

d1.update(d2)
print(d1)
