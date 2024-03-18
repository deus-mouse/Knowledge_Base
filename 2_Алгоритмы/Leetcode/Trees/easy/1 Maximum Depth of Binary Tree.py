# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


# Пример использования:
# Построение дерева для примера 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

s = Solution()

print(s.maxDepth(root))  # Должен вернуть 3

# Построение дерева для примера 2
# root = TreeNode(1)
# root.right = TreeNode(2)
#
# print(s.maxDepth(root))  # Должен вернуть 2