#initialize dictionary with default values
d1={}
n=int(input("Enter the count of dictionary :"))
for i in range(n):
    key=input("Enter key value")
    value=input("Enter value")
    d1[key]=value

print("Given dictionary  is:",d1)

d1.setdefault('colour','Yellow')
print("with default intialization:",d1)
