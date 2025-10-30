#palindrome check

words = ["madam", "apple", "level", "hello", "noon"]

for w in words:
    result = "Palindrome" if w == w[::-1] else "Not Palindrome"
    print(f"{w} → {result}")
