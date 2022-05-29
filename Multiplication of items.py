#Multiplication of items in dictionary
def mul(dict):
    s=1
    for i in dict:
        s=s*dict[i]
    return s
dict={'a':10, 'b':2, 'c':6}
print('mul:',mul(dict))
