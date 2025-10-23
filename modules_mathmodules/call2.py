import pattern
print("Welcome to pattern printing")
print("enter 1 for right triangle")
print("2.left triangle")
print("3.inverted right triangle")
print ("4.inverted left triangle")
opt=int(input("Enter any value"))
n=int(input("enter any value for number of rows"))
if opt==1:
    pattern.right_triangle(n)
elif opt==2:
    pattern.left_triangle(n)
elif opt==3:
    pattern.inverted_right(n)
elif opt==4:
    pattern.inverted_left(n)
else:
    print("invalid option")
