#program to get names until 'stop'

names=[]

while True:
    name=input("Enter a name (type 'stop' tostop):")
    if name.lower()=="stop":
        break
    names.append(name)

print(names)
