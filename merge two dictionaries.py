Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#To merge two dictionaries
d1={'a':100,'b':200}
d2={'x':300,'y':400}
d=d1.copy()
d.update(d2)
print(d)
{'a': 100, 'b': 200, 'x': 300, 'y': 400}
