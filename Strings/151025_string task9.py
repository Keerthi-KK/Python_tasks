#program to count vowels in a string 
text_to_check="Python Programming"
vowels="aeiou"
count=0

text=text_to_check.lower()

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            count+=1
print(count)
