# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))


# Пример использования
s = Solution()

root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.isValidBST(root1))  # Выведет: True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(s.isValidBST(root2))  # Выведет: False