cities=["Chennai","Coimbatore","Madurai","Trichy"]
print(cities)
cities_to_remove=input("Enter cities to remove")
if cities_to_remove in cities:
    cities.remove(cities_to_remove)
else: print("Cities not found in list")

print("Updated Cities list:")
print(cities)
