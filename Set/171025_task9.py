#program to convert set to string
s1=set()
n=5
for i in range(n):
    new=input("enter values to set ")
    s1.add(new)
print("given set is ",s1)
g=" ".join(s1)
print("set converted to string is :",g)
