#convert list to dictionary
keys=['Rash','kill','me']
values=[1,2,3]
print('original key list is:'+ str(keys))
print('original value list is:'+ str(values))
r={}
for key in keys:
    for value in values:
        r[key]=value
        values.remove(value)
        break
print('resultant dictionary is :'+str(r))


