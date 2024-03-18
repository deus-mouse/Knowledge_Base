# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        print(f'{mid=}')
        root = TreeNode(nums[mid])
        print(f'{root=}')
        print(f'{root.val=}')
        print('===========')
        root.left = self.sortedArrayToBST(nums[:mid])  # левое становится правым
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # правое становится левым

        return root


# Примеры использования
s = Solution()
nums1 = [-10, -3, 0, 5, 9]
root1 = s.sortedArrayToBST(nums1)
# Вывод результата для root1 требует обхода созданного дерева.

nums2 = [1, 3]
root2 = s.sortedArrayToBST(nums2)
# Вывод результата для root2 также требует обхода созданного дерева.