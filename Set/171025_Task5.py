#common elements in three lists using sets
l1=[1,2,3,4,5,6,"Preetha"]
l2=[10,20,30,40,"Preetha"]
l3=["Anitha","Preetha","Guhan"]

s1=set(l1)
s2=set(l2)
s3=set(l3)

s=s1.intersection(s2,s3)
print(s)

