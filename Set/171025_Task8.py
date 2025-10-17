#program to convert set to list
s1=set()
n=5
for i in range(n):
    new=int(input("enter values to set "))
    s1.add(new)
print("given set is ",s1)

l1=list(s1)
print("set converted to list is :",l1)
