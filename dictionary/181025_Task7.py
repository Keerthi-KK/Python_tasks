#remove a key from dictionary

d1={}
n=int(input("Enter the count of dictionary :"))
for i in range(n):
    key=input("Enter key value")
    value=input("Enter value")
    d1[key]=value

print("Given dictionary  is:",d1)
key=input("Enter any value to remove")
d1.pop(key)
print("After removing :",d1)
