# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''


# Для проверки, является ли данное число
# n степенью тройки, можно использовать несколько подходов. Один из простых способов — делить
# n на 3 в цикле до тех пор, пока
# n не станет равным 1, проверяя, что
# n делится на 3 на каждом шаге. Если на каком-то шаге
# n не делится на 3 и не равно 1,
# n не является степенью тройки.


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:  # Число должно быть положительным, чтобы быть степенью тройки
            return False
        while n % 3 == 0:  # Пока число делится на 3
            n /= 3  # Делим число на 3
            print(f'{n=}')
        return n == 1  # Если в результате получилась 1, число является степенью тройки


# Анализ Big O эффективности:
# Временная сложность: O(log3n)
# — потому что на каждом шаге цикла значение n уменьшается в три раза,
# что приводит к логарифмическому времени выполнения.
# Пространственная сложность: O(1)
# — используется константное количество памяти, не зависящее от размера входных данных.


s = Solution()
print(s.isPowerOfThree(27))  # Вывод: True
# print(s.isPowerOfThree(0))   # Вывод: False
# print(s.isPowerOfThree(-1))  # Вывод: False