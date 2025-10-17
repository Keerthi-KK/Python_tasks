#program to print right triangle

for i in range(5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
