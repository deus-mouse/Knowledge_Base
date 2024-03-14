# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''
from typing import List

x = 123  # 321
x = -123  # -321
x = 120  # 21


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        l = list(str(x))
        minus = x < 0
        left, right = 0, len(l) -1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
        res = ''.join([num for num in l if num != '-'])
        res = int(res) if not minus else -int(res)

        if res < INT_MIN or res > INT_MAX:
            return 0
        else:
            return res


    def reverse_GPT(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        print(f'{INT_MIN=}, {INT_MAX=}')

        # Handle negative numbers by storing the sign
        sign = -1 if x < 0 else 1
        x *= sign  # Make x positive

        # Reverse the digits of x
        reversed_x = int(str(x)[::-1])

        # Apply the sign back to reversed_x
        reversed_x *= sign

        # Check if reversed_x is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else:
            return reversed_x


res = Solution()
print(res.reverse_GPT(x))
