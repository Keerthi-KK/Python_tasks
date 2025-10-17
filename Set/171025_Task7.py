#program to convert set to tuple and tuple to set

s1={5,3,8,9,10,8,9,3}
print("Given set is :",s1)
t1=tuple(s1)
print("set converted to tuple is :",t1)

t2=(55,65,75,85,75,55)
print("Given tuple is:",t2)
s2=set(t2)
print("tuple converted to set is",s2)
