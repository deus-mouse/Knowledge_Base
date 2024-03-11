 # https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/'''
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''
from typing import List

nums = [0,1,0,3,12]  # [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
        nums.extend([0] * count)
        return nums



s = Solution()
print(s.moveZeroes(nums))
# print(s.moveZeroes(nums))
