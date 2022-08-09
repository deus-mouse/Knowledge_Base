# дана последовательность положительных
# чисел длиной N и число Х
# Нужно найти два различных числа А и В
# из последовательности, таких что А + В = Х
# или вернуть пару 0, 0, если такой пары чисел нет

import random
# print([random.randint(0, 100) for _ in range(20)])
data = [20, 84, 77, 37, 43, 49, 56, 51, 50, 100, 10, 80, 23, 66, 28, 26, 38, 89, 80, 17]

# Решение за 0(N2) (с ошибкой) -> могут втретиться одинаковые числа
# Переберем число А за O(N). Переберем число В за O(N).
# Если их сумма равна Х, то вернем эту пару
def foo1(data, x):
    A, B = 0, 0
    for a in data:
        for b in data:
            if a + b == x:
                A, B = a, b
    return A, B


print(f'{foo1(data, 60)}')
print(f'{foo1(data, 14)}')


# Решение за 0(N2)
def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0


print(f'{twotermswithsumx(data, 60)}')
print(f'{twotermswithsumx(data, 14)}')


# Решение за 0(N)
# Будем хранить все уже обработанные числа в множестве.
# Если очередное число nownum, а Х — nownum есть
# в множестве, то мы нашли слагаемые
def twotermswithsumx2(nums, x):
    prevnums = set()
    for nownum in nums:
        if nownum - x in prevnums:
            return nownum, nownum - x
        prevnums.add(nownum)
    return 0, 0

print(f'{twotermswithsumx2(data, 60)}')
print(f'{twotermswithsumx2(data, 14)}')

