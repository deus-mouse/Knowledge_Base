# Дана последовательность чисел длиной N
# Найти минимальное четное число в последовательности
# или вывести -1, если такого не существует.


import math

seq = [1, 7, 3, 4, 2, 4]
# seq = [-1, -2, -3, -4, -2]
# seq = [0, 0, 0]
# seq = [1, 3, 5]


# мое решение
def find(seq):
    ans = -1
    min = math.inf
    for i in range(0, len(seq)):
        if seq[i] % 2 == 0 and min > seq[i] and seq[i] != 0:
            min = seq[i]
            ans = min
    return print(f'1 -> {ans=}')

find(seq)


# Решение
# В переменную для ответа положим -1. Если очередное число четное,
# а ответ равен -1 или ответ больше текущего числа, то запишем в ответ
# текущее число

def findmineven(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        # if (seq[i] % 2 == 0) and (ans == -1 or seq[i] < ans):
        if (seq[i] % 2 == 0) and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return print(f'{ans=}')

findmineven(seq)