# Write a Python Program to convert the elements of two lists into key-values pairs of a dictionary.

country=["USA","INDIA","GERMANY","FRANCE"]
cities={"WASHINGTON","NEW DELHI","BERLIN","PARIS"}
z=zip(country,cities)
d=dict(z)
for k in d:
  print(k,d[k])
