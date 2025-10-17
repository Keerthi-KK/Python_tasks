#Count Even Numbers - From a list [1, 2, 3, 4, 5, 6, 7, 8], count how many are even.

even=0
l1=[1,2,3,4,5,6,7,8]

for i in l1:
    if i%2==0:
        print("Even number")
        even+=1
    else:
        print("odd number")
        
