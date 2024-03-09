# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

nums = [0,0,1,1,1,2,2,3,3,4]
print(f'{len(nums)=}')


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for index in range(len(nums) - 1, 0, -1):  # НАДО В ОБРАТНОМ ПОРЯДКЕ Т.К. ИНДЕКСЫ СМЕЩАЮТСЯ
            if nums[index] == nums[index - 1]:
                del nums[index]
            else:
                k += 1
        # return f'{k}, nums = {nums}'
        return k


result = Solution.removeDuplicates(Solution, nums)
print(result)


