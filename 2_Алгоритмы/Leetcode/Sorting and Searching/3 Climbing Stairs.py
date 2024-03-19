# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''


class Solution:
    def climbStairs_GPT(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Инициализация первых двух значений
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first, second = second, third

        return second



# Примеры использования
s = Solution()
print(s.climbStairs_GPT(2))
print(s.climbStairs_GPT(3))
