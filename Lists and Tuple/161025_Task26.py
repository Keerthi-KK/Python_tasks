#Find Smallest Number - Find the smallest value in (45, 12, 89, 33, 67) using a loop.

t = (45, 12, 89, 33, 67)
smallest = t[0]
for i in t:
    if i < smallest:
        smallest = i
print("Smallest number:", smallest)
