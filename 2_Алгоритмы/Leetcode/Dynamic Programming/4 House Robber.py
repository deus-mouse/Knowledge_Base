# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# алгоритм КАДАНА

# Чтобы найти подмассив с наибольшей суммой в массиве nums,
# можно использовать алгоритм, известный как алгоритм КАДАНА.
# Этот алгоритм позволяет находить максимальную сумму подмассива,
# используя однопроходный метод,
# который итеративно обновляет текущую сумму подмассива и максимальную сумму подмассива

from typing import List

nums = [2,7,9,3,1]
nums = [2,1,1,2]


class Solution:
    def rob_GPT(self, nums):
        if not nums:  # Проверка на пустой список
            return 0
        if len(nums) <= 2:  # Если домов меньше трех, вернуть максимальное значение
            return max(nums)

        dp = [0] * len(nums)  # Инициализация списка для динамического программирования
        dp[0] = nums[0]  # Первый дом можно взломать без ограничений
        dp[1] = max(nums[0], nums[1])  # Выбираем максимальное значение из первых двух домов

        for i in range(2, len(nums)):  # Начинаем с третьего дома
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Максимум из: не взламывать текущий дом, взломать текущий дом

        return dp[-1]  # Возвращаем максимальную сумму, которую можно украсть

    def rob(self, nums: List[int]) -> int:
        profit_1 = 0
        profit_2 = 0

        for i in nums[::2]:
            profit_1 += i

        for i in nums[1::2]:
            profit_2 += i

        return max(profit_1, profit_2)


# Примеры использования
s = Solution()
# print(s.rob(nums))
print(s.rob_GPT(nums))
