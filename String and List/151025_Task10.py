#string reversal without using slicing

s="Hi , Good morning to all"
print(s[::-1])
reversed_string=" "
for ch in s:
    reversed_string=ch+reversed_string
print(reversed_string)
    
    
