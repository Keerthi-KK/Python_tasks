#Multiply each number of a given list with a given number (using math function)
import math

numbers = [2, 4, 6, 8, 10]
n = int(input("Enter a number to multiply: "))

result = list(map(lambda x: math.prod([x, n]), numbers))

print("Result list:", result)
