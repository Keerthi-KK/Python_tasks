#distance with inbuilt function

import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

p1 = (x1, y1)
p2 = (x2, y2)
distance = math.dist(p1, p2)
print("Distance using inbuilt dist():", distance)
