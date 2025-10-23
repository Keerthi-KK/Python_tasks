#program to convert radian to degree
import math

radian = float(input("Enter value in radians: "))
degree = radian * (180 / math.pi)

print("Value converted to degrees is(manual):", degree)

degree2= math.degrees(radian)
print("converted to degree is (using inbuilt):",degree2)
