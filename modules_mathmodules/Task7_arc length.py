#Arc length of a circle

import math
r =  int(input("Enter r value:"))
angle = float(input("Enter angle value:"))
arc_length = 2 * math.pi * r * (angle / 360)
print("Arc length:", arc_length)
