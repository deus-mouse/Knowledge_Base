'''
D. Генерация скобочных последовательностей

Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, 
упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.
Желательно получить решение, которое работает за время, 
пропорциональное общему количеству правильных скобочных последовательностей в ответе, 
и при этом использует объём памяти, пропорциональный n.
'''

import sys

n = int(sys.stdin.readline().strip())

def parentheseser(output, open, closed, n):
    if len(output) == n*2:
        if open == closed:
            print(f'{output=}')
    if open < n:
        parentheseser(output + '(', open + 1, closed, n)
    if closed < open:
        parentheseser(output + ')', open, closed + 1, n)

def foo(n):
    parentheseser('', 0, 0, n)

foo(n)