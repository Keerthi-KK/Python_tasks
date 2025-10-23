    
def get_list(n):
    lst = []  
    for i in range(n):
        value = int(input(f"Enter value {i+1}: "))
        lst.append(value)
    return lst


def print_list(lst):
    print("The list elements are:")
    for val in lst:
        print(val)

def check_even(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
