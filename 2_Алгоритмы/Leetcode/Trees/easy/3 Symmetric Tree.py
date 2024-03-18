# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:  # Оба узла пусты (базовый случай симметрии)
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)  # Значения обоих узлов равны, и рекурсивные вызовы для левого поддерева одного узла и правого поддерева другого узла, а также для правого поддерева первого узла и левого поддерева второго узла возвращают True.

        if not root:
            return True
        return isMirror(root.left, root.right)


# Пример использования

s = Solution()
root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(2, TreeNode(4), TreeNode(3)))
print(s.isSymmetric(root1))  # Выведет: True

root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                 TreeNode(2, None, TreeNode(3)))
print(s.isSymmetric(root2))  # Выведет: False