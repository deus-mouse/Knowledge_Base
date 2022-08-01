'''
ДАны три целых числа a, b, c.
Найдите все корни уравнения ax(2) + bx + c = 0
и выведите их в порядке возрастания
'''
from math import sqrt

def foo(a, b, c):
    if a == 0:
        if b != 0:
            print(-c / b)
        if b == 0 and c == 0:
            print('Infinite number of solutions')
    else:
        d = b ** 2 - 4 * a * c
        print(sqrt(d))
        if d == 0:
            x1 = -b / (2 * a)
            print(x1)
        elif d > 0:
            x1 = (-b - sqrt(d)) / (2 * a)
            x2 = (-b + sqrt(d)) / (2 * a)
            if x1 < x2:
                print(x1, x2)
            else:
                print(x2, x1)
