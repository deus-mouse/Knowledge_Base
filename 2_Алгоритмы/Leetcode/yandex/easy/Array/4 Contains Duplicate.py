# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
from typing import List
from collections import defaultdict


nums = [1,2,3,1]  # True
# nums = [1,2,3,4]  # False


class Solution:
    def containsDuplicate_gpt(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
            if dd[i] > 1:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
        if max(dd.values()) > 1:
            return True
        else:
            return False


s = Solution()
# print(s.containsDuplicate(nums))
# print(s.containsDuplicate_gpt(nums))
print(s.containsDuplicate2(nums))
