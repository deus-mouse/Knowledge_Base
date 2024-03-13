# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
from typing import List
from collections import defaultdict

nums = [4,1,2,1,2]  # 4


class Solution:
    def singleNumber_gpt(self, nums: List[int]) -> int:  # XOR
        result = 0
        for num in nums:
            print(f'{result=}, {num=}')
            result ^= num  # XOR, по сути это сумма всех чисел. только при вхождении того же элемента, он уже будет вычтен
            print(f'-> {result=}')
        return result

    def singleNumber(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1

        for k, v in dd.items():
            if v == 1:
                return k


s = Solution()
# print(s.singleNumber(nums))
print(s.singleNumber_gpt(nums))