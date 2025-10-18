#create a new dictionary by extracting keys from another dictionary

d1={'a':1,'b':2,'c':3,'d':4}
keys=['a','c']
new_dict={}
for key,value in d1.items():
    if key in keys:
        new_dict[key]=value
print(new_dict)
