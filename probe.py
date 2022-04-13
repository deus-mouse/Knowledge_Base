
a = [1]
b = a

print(a is b)

c = a.copy()
print(c)
print(a is c)

a = [2]
print(f'{c=}')