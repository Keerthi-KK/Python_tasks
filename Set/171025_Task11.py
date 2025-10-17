#convert set to dictionary

s1={55,66,"nisha","new"}
d1=dict.fromkeys(s1,0)
print("set converted to dictionary is :",d1)
d2={item: i for i,item in enumerate(s1)}
print("set converted to dictionary is :",d2)
s2={('a',2),('m','s'),('g',5)}
d3=dict(s2)
print("set converted to dictionary is:",d3)
