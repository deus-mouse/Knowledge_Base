# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

# алгоритм КАДАНА

# Чтобы найти подмассив с наибольшей суммой в массиве nums,
# можно использовать алгоритм, известный как алгоритм КАДАНА.
# Этот алгоритм позволяет находить максимальную сумму подмассива,
# используя однопроходный метод,
# который итеративно обновляет текущую сумму подмассива и максимальную сумму подмассива

from typing import List

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # алгоритм КАДАНА
        current_sum = max_sum = nums[0]  # Инициализируем текущую и максимальную сумму первым элементом
        for num in nums[1:]:  # Проходим по массиву, начиная со второго элемента
            # print(f'{num=}')
            current_sum = max(num, current_sum + num)  # Обновляем текущую сумму наибольшим значением между текущим элементом и суммой с текущим элементом
            # print(f'{current_sum=}')
            max_sum = max(max_sum, current_sum)  # Обновляем максимальную сумму, если текущая сумма больше максимальной
            # print(f'{max_sum=}')
            # print('============')
        return max_sum  # Возвращаем максимальную сумму подмассива


# Примеры использования
s = Solution()
print(s.maxSubArray(nums))
