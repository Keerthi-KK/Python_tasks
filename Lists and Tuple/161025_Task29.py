#Count Vowels - Create a tuple of letters and count how many vowels are there using a loop.
t = ('a', 'b', 'e', 'i', 'o', 'u', 'x', 'y')
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for ch in t:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
