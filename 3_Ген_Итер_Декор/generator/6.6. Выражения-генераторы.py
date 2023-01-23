
iterator = ('Привет' for i in range(3))

# l_iterator = list(iterator)
# print(f'{l_iterator=}')
# l_iterator=['Привет', 'Привет', 'Привет']

for x in iterator:
    print(f'{x=}')

# после того как выражение-генератор было использовано, оно не может быть перезапущено или использовано снова.


# Фильтрация значений

even_squares = (x * x for x in range(10) if x % 2 == 0)
l_even_squares = list(even_squares)
print(f'{l_even_squares=}')


for x in ('Buongiorno' for i in range(3)):
    print(f'{x=}')


# Круглые скобки, окружающие выражение-генератор, могут быть опущены
s = sum(x * 2 for x in range(10))






