def sum(dict):
    s=0
    for i in dict:
        s=s+ dict[i]
    return s
dict={'a':100,'b':500,'c':200}
print('sum:',sum(dict))
