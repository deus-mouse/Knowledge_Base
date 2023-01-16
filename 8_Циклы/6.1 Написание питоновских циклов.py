my_items = ['a', 'b', 'c']

# С-подобная кострукция
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1


for i in my_items:
    print(i)

# если нужен индекс
# print(f'{enumerate(my_items)=}')
for i, item in enumerate(my_items):
    print(f'{i}: {item}')
# 0: a
# 1: b
# 2: c


emails = {'Боб': 'bob@example.com',
          'Алиса': 'alice@example.com',}

for name, email in emails.items():
    print(f'{name} -> {email}')
# 'Боб -> bob@example.com'
# 'Алиса -> alice@example.com'


a, n, s = 0, 10, 2  # от, до, шаг
# если требуется управлять размером шага индекса?
for i in range(a, n, s):
    print(i)
