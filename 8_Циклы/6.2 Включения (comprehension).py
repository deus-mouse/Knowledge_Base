squares = [x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


my_items = ['a', 'b', 'c']
f = [item * 3 for item in my_items]
# ['aaa', 'bbb', 'ccc']


# С фильтрацией
even_squares = [x * x for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]


# включение в множество
my_set = {x * x for x in range(-9, 10)}
# {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}  неупорядочено


# включение в словарь:
my_dict = {x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


(print())