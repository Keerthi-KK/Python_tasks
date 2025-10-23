#Distance between two points (without dist())

import math
x1=int(input("enter x1 value:"))
y1 =int(input("enter y1 value:"))
x2=int(input("enter x2 value:"))
y2 = int(input("enter y2 value:"))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)
