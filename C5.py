# Write a Python Program to sort the elements of a dictionary.

c={10:"RED",35:"GREEN",15:"BLUE",25:"WHITE"}
c1=sorted(c.items(),key= lambda t: t[0])
print(c1)
c2=sorted(c.items(),key= lambda t: t[1])
print(c2)
