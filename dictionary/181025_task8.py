#find the size of dictionary

d1={}
n=int(input("Enter the count of dictionary :"))
for i in range(n):
    key=input("Enter key value")
    value=input("Enter value")
    d1[key]=value

print("Given dictionary  is:",d1)
print("length of the dictionary is ",len(d1))
