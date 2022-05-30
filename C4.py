# Write a Python Program to find the number of occurences of each letter in a String using Dictionary.

str=input("Enter String")
dict={}
for x in str:
  dict[x]=dict.get(x,0)+1
for k,v in dict.items():
  print(k,v)
