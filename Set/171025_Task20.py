#no of vowels in each name in a set

names = {"Kumar", "Rakul", "Sukumar", "Ankush", "Rakesh", "Mukul", "Keerthi"}
vowel={'a','e','i','o','u'}
for name in names:
    count = 0 
    for letter in name.lower():  
        if letter in vowel:    
            count += 1
    print(f"{name} → {count} vowels")
