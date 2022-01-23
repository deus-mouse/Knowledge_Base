# ГЕНЕРАТОР

def fibo_func1(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibo = fibo_func1(100)
for value in fibo:
    print(value)

#  Бесконечный генератор

def fibo_func2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibo2 = fibo_func2()
for value in fibo2:
    print(value)
    if value > 10 ** 2:
        break

#можно использовать return = raise StopEteration

def fibo_func3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 2:
            return

fibo3 = fibo_func3()
for value in fibo3:
    print(value)


# можно прерывать несколько вложенных циклов

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

def result_func(list_1, list_2):
    for x in list_1:
        for y in list_2:
            yield x, y, x*y

for x, y, result in result_func(list_1, list_2):
    print(x, y, result)
    if result == to_find:
        print('Found!!!')
        break

# так же может принимать значение

def solar_system_func(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value:
            data.append(new_value)

solar_system = solar_system_func('Mercury', 'Venus', 'Earth')
for planet in solar_system:
    print(f'I am - {planet}')
    if planet == 'Venus':
        planet = solar_system.send('Mars')
        print(f'I am - {planet}')

