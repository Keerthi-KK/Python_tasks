#find difference between two lists

l1=[1,2,3,4,5,6]
l2=[2,6,17,23,45]

s1=set(l1)
s2=set(l2)

s3=s1.difference(s2)
print(s3)
