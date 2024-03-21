# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''

import random


class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = list(nums)

    def reset(self):
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        # алгоритм Фишера-Йетса
        # для случайной перетасовки массива.
        # Он проходит по массиву,
        # на каждом шаге выбирая случайный индекс из необработанной части массива
        # и обменивая текущий элемент с элементом под выбранным индексом.
        for i in range(len(self.nums)):
            swap_idx = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(f'{param_1=}')
param_2 = obj.shuffle()
print(f'{param_2=}')
