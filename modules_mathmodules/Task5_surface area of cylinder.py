#Surface area and volume of a cylinder

import math
r = int(input("Enter r value:"))
h = int(input("Enter h value:"))
surface_area = 2 * math.pi * r * h + 2 * math.pi * r**2
volume = math.pi * r**2 * h
print("Surface area of cylinder:", surface_area)
print("Volume of cylinder:", volume)
