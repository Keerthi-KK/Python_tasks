#program to print right triangle
def right_triangle(n):    
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end=" ")
        for k in range(0,i+1):
            print("*",end=" ")
        print()

#left triangle
def left_triangle(n):
    for u in range(1,n+1):
        for j in range(1,u+1):
            print("*",end=" ")
        print()
#inverted right triangle
def inverted_right(n):  
    for i in range(n,0,-1):
        for k in range(0,n-i):
            print(" ",end=" ")        
        for j in range(1,i+1):
            print("*",end=" ")
        print()
def inverted_left(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

