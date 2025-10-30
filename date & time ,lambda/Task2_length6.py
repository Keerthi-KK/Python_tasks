#values of length six in given list 
words = ["orange", "banana", "apple", "mangoes", "cherry", "tomato"]

length_six = []
for word in words:
    if len(word) == 6:
            length_six.append(word)

print("Words with length 6:", length_six)
