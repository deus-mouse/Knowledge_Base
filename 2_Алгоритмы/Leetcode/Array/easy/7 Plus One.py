# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
from typing import List

digits = [1,2,3]  # [1,2,4]


class Solution:
    def plusOne_gpt(self, digits: List[int]) -> List[int]:
        # Reverse the digits for easier manipulation
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            if digits[i] + carry == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
                break
        if carry:
            digits.append(1)
        # Reverse back before returning
        return digits[::-1]
    
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''.join([str(num) for num in digits])
        res = int(res) + 1
        res = [int(num) for num in str(res)]
        return res




s = Solution()
print(s.plusOne(digits))
print(s.plusOne_gpt(digits))
