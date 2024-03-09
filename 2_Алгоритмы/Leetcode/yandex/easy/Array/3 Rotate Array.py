# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
from typing import List


nums = [1,2,3,4,5,6,7]  # [5, 6, 7, 1, 2, 3, 4]
k = 3

class Solution:

    def rotate_gpt(self, nums: List[int], k: int) -> None:
        k = k % len(nums)  # на случай, если k больше длины списка

        nums = nums[-k:] + nums[:-k]
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(0, k):
            nums.insert(0, nums.pop(-1))
        return nums


s = Solution()

# print(s.rotate(nums, k))
print(s.rotate_gpt(nums, k))
