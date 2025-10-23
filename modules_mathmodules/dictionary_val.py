#sum of values in dictionary

def get_value(n):
    d1={}
    for i in range(n):
        key=input("Enter key value")
        value=int(input("Enter value"))
        d1[key]=value
    return d1
def print_value(d1):
    return d1
def sum_value(d1):
        var_sum =sum(d1.values())
        return var_sum


