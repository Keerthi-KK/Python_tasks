#Combination (nCr) without inbuilt function

#nCr=n!/r!(n−r)!​

import math
n = int(input("enter n value:"))
r = int(input("enter r value:"))
combination = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print("Combination (nCr):", combination)
