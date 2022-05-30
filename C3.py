# Write a Python program to create a D ictionary from keyboard and display the elements.

x={}
n=int(input("Enter the no. of key-value pairs"))
for i in range(n):
  k=eval(input())
  v=eval(input())
  x.update({k:v})
print(x)
