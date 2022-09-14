"""
Как решать дробно-рациональные уравнения? | Математика
https://www.youtube.com/watch?v=mSEsSHjyqOk

A. Сложное уравнение
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0

Формат ввода
Вводятся 4 числа: a, b, c и d; c и d не равны нулю одновременно.

Формат вывода
Необходимо вывести все целочисленные решения, если их число конечно,
“NO” (без кавычек), если целочисленных решений нет,
и “INF” (без кавычек), если их бесконечно много.

Пример 1
Ввод
1
1
2
2
Вывод
NO

Пример 2
Ввод
2
-4
7
1
Вывод
2

Пример 3
Ввод
35
14
11
-3
Вывод
NO
"""

import sys

input = []
# for _ in range(4):
#     char = int(sys.stdin.readline().strip())
#     input.append(char)

# старое решение - неверное
def foo_1(input):
    a, b, c, d = input
    res = set()
    for x in range(100):
        if (c * x != -d) and (a * x == -b):
            res.add(x)

    if res:
        [print(x) for x in res]
    elif len(res) > 10:
        print('INF')
    else:
        print('NO')


def foo_2(input):
    res = set()
    a, b, c, d = input
    x = b / a
    if x > 0 and isinstance(x, int):
        res.add(x)



# foo_1([1, 1, 2, 2])
# foo_1([2, -4, 7, 1])
# foo_1([35, 14, 11, -3])




