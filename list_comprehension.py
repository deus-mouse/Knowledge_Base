# 1
squares = {x ** 2 for x in range(10)}
print(f'{squares=}')  # squares={0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


# 2 Гораздо удобнее итерироваться по двум спискам:
first = []
for x in range(1, 5):
  for y in range(5, 1, -1):
    if x != y:
      first.append((x, y))
print(f'{first=}')

second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
print(f'{second=}')

print(f'{first==second=}')  # first==second=True


# 3 Отличный пример из документации (раскрытие списка списков), усложним его:
vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
vec_2 = [digit for lst in vec for elem in lst for digit in elem]
print(f'{vec_2=}')  # vec_2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# 4 Подобным образом с помощью генераторов списков мы можем создать словарь:
d = dict([(key, value) for (key, value) in zip([1, 2, 3], ['a', 'b', 'c'])])
print(f'{d=}')  # d={1: 'a', 2: 'b', 3: 'c'}


# 5 И тут нас ожидает приятная новость — в python есть и генераторы словарей,
# записываются так же, как и генераторы списков, только в фигурных скобках { ... }:
k = {key: value for key, value in zip([1, 2, 3], ['a', 'b', 'c'])}
print(f'{k=}')  # k={1: 'a', 2: 'b', 3: 'c'}
