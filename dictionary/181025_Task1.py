#to check if given key exists in a dictionary

n=int(input("Enter the count"))
d={}
for i in range(n):
    key=input("Enter key value")
    value=input("Enter value")
    d[key]=value

print(d)

to_check=input("Enter any key to search")
for to_check in d:
    if to_check in d:
        print("found")
        break
    else: print("not found")
