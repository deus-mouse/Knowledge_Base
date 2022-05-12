'''
C. Удаление дубликатов

Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, 
т.е., использует лишь константный объем памяти в процессе работы.
'''


# попытка через ввод данных в консоль
import sys

n = int(sys.stdin.readline().strip())
d = list()
prev = None
for _ in range(n):
    new = int(sys.stdin.readline().strip())
    if new != prev:
        print(new)
        prev = new


# попытка через файл
# with open('input.txt') as file:
#     l = list()
#     for char in file:
#         l.append(int(char))
#     l.pop(0)
#
# new_l = sorted(set(l))
#
# with open("output.txt", "w") as file:
#     for item in new_l:
#         print(item, file=file, sep="\n")
