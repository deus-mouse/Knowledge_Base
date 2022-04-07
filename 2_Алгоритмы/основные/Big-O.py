# Оценка сложности алгоритма. Big O.
# Идея не в том, чтобы измерять время выполнения алгоритма,
# а измерять такую характеристику как асимптотическое время выполнения алгоритма.
# Асимптотика - поведение функции при стремлении аргумента к бесконечности.
# Позволяет сравнивать алгоритмы, не обращая внимания на детали реализации (язык, компилятор, мощность компьютера).

# От эффективного к менее эффективному:
# O(1) - set() т.к. хранится в виде хэш-таблицы / добавление в конец списка
# O(n) - растет пропорциоанльно, линейно с ростом аргумента n / удаление элемента из начала, потмоу что другие должны сместится
# O(log n)
# O(n**2)
# O(2n)
# ... есть еще, но это самые распространенные.

# Таблица эффективности
# https://works.doklad.ru/view/w4c2OLj2iMk.html

from random import randint
from datetime import datetime

# linear_search

# x = [x for x in range(0, 1_000_000)]
a = [randint(0, 1_000_000) for x in range(0, 1_000_000)]
# print(f"{x=}")

a_set = set(a)
# print(f"{x_set=}")

a_set_sorted = sorted(a_set)
print(f"{a_set_sorted=}")

print(len(a))
print(len(a_set))
print(len(a_set_sorted))

# x = 1_000_000
x = 100_000

def linear_search(array, x):
    for index in range(len(array)):
        if array[index] == x:
            return index
            # return array.index(x)
    return -1

def binary_search(array, x):
    if sorted(array) != array:
        raise ValueError("Array must be sorted!")

    start = 0
    end = len(array)

    while start <= end:
        center = (start + end) // 2

        if array[center] == x:
            return center

        elif array[center] < x:
            start = center + 1

        elif array[center] > x:
            end = center - 1

    return -1




start = datetime.now()
l_search = linear_search(a_set_sorted, x)
time = datetime.now() - start
print(f"{l_search=}, {time=}")

start = datetime.now()
b_search = binary_search(a_set_sorted, x)
time = datetime.now() - start
print(f"{b_search=}, {time=}")