# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/

'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''
from typing import List



class Solution:
    def missingNumber_GPT(self, nums: List[int]) -> int:
        # Для диапазона от 0 до n сумма всех чисел равна S = n⋅(n+1) / 2
        # Если вычесть из этой суммы сумму всех элементов массива, получим пропущенное число.

        n = len(nums)  # Количество элементов в массиве
        total_sum = n * (n + 1) // 2  # Сумма всех чисел от 0 до n
        print(f'{total_sum=}')
        array_sum = sum(nums)  # Сумма элементов массива
        return total_sum - array_sum  # Пропущенное число

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = [f for f in range(1, n+1)]
        print(f'{l=}')

        diff = set(l) - set(nums)
        print(f'{diff=}')
        return list(diff)[0]




s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber_GPT([1]))
print(s.missingNumber_GPT([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Вывод: 8

