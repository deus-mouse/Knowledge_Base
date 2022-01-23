# Предположим есть функция с тяжеловесными вычислениями:
# найти количество цифр в произведении 5000-х степеней чисел

def calculator(*args):
    total = 1
    for number in args:
        total *= number ** 9000
    return len(str(total))

# и нам надо засечь время выполнения функции

import time
started_at = time.time()
result = calculator(2134, 7322, 9586, 8584)
print(result)
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Elapsed 1 = {elapsed}')


# Вообще, учет времени выполнения - достаточно типичная ситуация, и хочется сделать функцию-помощника
#
# Напишем функцию высшего порядка, на вход которой передается другая функция и параметры с которыми надо её вызвать

def time_track(func, *args):
    started_at = time.time()
    result = func(*args)
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Elapsed 2 = {elapsed}')
    return result

timed_calc = time_track(calculator, 2134, 7322, 9586, 8584)
print(result)

# Но можно пойти еще глубже - пусть time_track еще и возвращает функцию.
# Функцию, которая заместит оригинальную func.

def time_track_2(func):
    def surrogate(*args):
        started_at = time.time()
        result = func(*args)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Elapsed 3 = {elapsed}')
        return result
    return surrogate

calculator = time_track_2(calculator)
result = calculator(2134, 7322, 9586, 8584)
print(result)

# а можно вообще сделать так


# и теперь digits - почти та же функция, но не та. Она отдекорирована функцией time_track
# за счет *args, **kwargs внутренняя surrogate принимает все параметры
# и тут же передает их в декорируемую функцию
#
# в пайтон есть синтаксический сахар для декораторов. выглядит он так

@time_track_2
def calculator_2(*args):
    total = 1
    for number in args:
        total *= number ** 9000
    return len(str(total))

result = calculator_2(2134, 7322, 9586, 8584)
print(result)



# Это аналог digits = time_track(digits)
#
# Минусы декораторов:
#  - затруднена отладка
#  - нужно делать определенные действия, что бы сохранить аттрибуты декорерируемой функции (см functools.wraps)



# Для тех, у кого голова еще не закружилась - можно пойти еще глубже.
#
# Напишем функцию, которая принимает параметры и возвращает декоратор

def get_time_track(precision):
    def time_track(func):
        def surrogate(*args):
            started_at = time.time()
            result = func(*args)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Elapsed 4 = {elapsed}')
            return result
        return surrogate
    return time_track

calculator_3 = get_time_track(8)
calculator_3 = calculator_3(calculator)
result = calculator_3(2134, 7322, 9586, 8584)
print(result)

# Синтаксический сахар нам поможет сделать все компактно

@get_time_track(8)
def calculator_3(*args):
    total = 1
    for number in args:
        total *= number ** 9000
    return len(str(total))

get_time_track_8 = calculator_3(2134, 7322, 9586, 8584)
print(get_time_track_8)


# Да, get_time_track - монстр с тремя -головами- уровнями сложности...
# Давайте разберем что происходит.





# Писать и отлаживать декораторы с параметрами сложно. Но увлекательно.
