import lists

n=int(input("Enter the number of values in the list"))
result=lists.get_list(n)
print("final list:",result)

print("\nChecking even/odd:")
for num in result:
    lists.check_even(num)
