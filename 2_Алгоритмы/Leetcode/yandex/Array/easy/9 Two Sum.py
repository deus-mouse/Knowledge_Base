 # https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from typing import List

nums = [2,7,11,15]
target = 9  # Output: [0,1]

nums = [0,4,3,0]
target = 0  # Output: [0, 3]



class Solution:
    def twoSum_gpt(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        d = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                answer = [d[nums[i]], i]
                break
            else:
                d[diff] = i  # {7: 0}
        return answer




s = Solution()
print(s.twoSum(nums, target))
# print(s.moveZeroes(nums))
