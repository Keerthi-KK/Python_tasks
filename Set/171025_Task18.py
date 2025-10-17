#program to find the prime numbers in a set

n={2,3,4,5,6,7,8,9,10,11,12,13,14,15}
prime=set()

for i in n:
    if i>1:
        is_prime_checker=True
        for j in range(2,i):
            if i%j==0:
               is_prime_checker=False
               break
        if is_prime_checker:
            prime.add(i)

print("original set=",n)
print("Prime numbers=",prime)
