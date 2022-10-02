

print(10%3)


l = [1, 2, 3, 4, 5, 4, 3, 2, 1]
l_2 = [1, 2, 1, 2, 2, 1, 2, 1]
print(f'{len(l)/2=}')
print(f'{type(len(l)/2)=}')
print(f'{int(len(l)/2)=}')

print(f'{len(l_2)/2=}')
print(f'{type(len(l_2)/2)=}')
print(f'{int(len(l_2)/2)=}')


def foo(payload):
    center = len(payload) // 2 if len(payload) % 2 else (len(payload) // 2 - 1)
    print(f'{center=}')


foo(l)
foo(l_2)

for i in range(1):
    print(f'{i=}')