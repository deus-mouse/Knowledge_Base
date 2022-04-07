'''
B. Последовательно идущие единицы

Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.
'''


# попытка через ввод данных в консоль
import sys

n = int(sys.stdin.readline().strip())
d = list()
for n in range(n):
    d.append(int(sys.stdin.readline().strip()))

current = 0
best = 0
for char in d:
    if int(char) == 1:
        current += 1
    else:
        current = 0
    best = max(current, best)

print(best)


# попытка через файл
# with open('input.txt') as file:
#     current = 0
#     best = 0
#     for char in file:
#         if int(char) == 1:
#             current += 1
#         else:
#             best = max(current, best)
#             current = 0
#
# with open("output.txt", "w") as file:
#     print(best, file=file)

