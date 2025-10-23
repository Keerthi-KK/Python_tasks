def prime(n):
    if n<=1:
        print("not a prime number")
        return
    for i in range(2,n):
        if n%i ==0:
            print("Not a prime number")
            return
        else:
            print("Prime number")
            return

def perfect_number(n):
    if n<=0:
        print (" not a perfect number")
        return
    sum_div=0
    for i in range(1,n):
        if n%i ==0:
            sum_div+=i
        if sum_div==n:
            print("perfect number")
            return
        else:
            print("not a perfect number")
            return

def armstrong_number(n):
    num_str=str(n)
    power=len(num_str)
    total=0
    for digit in num_str:
        number=int(digit)
        result=number**power
        total=total+result
    if total==n:
        print ("armstrong number")
        return
    else:
        print("not a armstrong number")
        return
    
    
    
        
