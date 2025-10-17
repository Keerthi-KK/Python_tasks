items=[]

for i in range(5):
    item=input("Enter an item :")
    items.append(item)
print("List before removing :",items)
remove_item=input("Enter item to remove:")
if remove_item in items:
    items.remove(remove_item)
    print("updated list",items)
else:
    print("item not found")
