# remove duplicate values
d={'a':10,'b':20,'c':30,'d':20,'e':10}
print('The original dictonary is:'+str(d))
t=[]
r=dict()
for key,val in d.items():
    if val not  in t:
        t.append(val)
        r[key]=val
print('dictionary agter value removal:'+str(r))
