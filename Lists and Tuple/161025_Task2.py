#program to create a list of 5 fruits and print it
l=["Apple","Banana","Dragon fruit","Pineapple","Strawberry"]
print(l)
new_fruit=input("Enter any fruit to add")
l.append(new_fruit)
print("After adding new fruit")
print(l)
remove_fruit=input("Remove fruit name:")
l.remove(remove_fruit)
print("After removing fruit")
print(l)
    
