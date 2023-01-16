my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

for i in my_items:
    print(i)


print(f'{enumerate(my_items)=}')
for i, item in enumerate(my_items):
    print(f'{i}: {item}')