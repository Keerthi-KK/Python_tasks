#program to remove digitsfrom a string

text="Python123 is fun 456"
result=' '.join([ch for ch in text if not ch.isdigit()])
print(result)
