# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode):
        def isMirror(l: TreeNode, r: TreeNode):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)

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



