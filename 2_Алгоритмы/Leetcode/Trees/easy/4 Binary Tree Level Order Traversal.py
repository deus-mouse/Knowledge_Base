# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

# Примеры использования
s = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.levelOrder(root1))  # Выведет: [[3],[9,20],[15,7]]

root2 = TreeNode(1)
print(s.levelOrder(root2))  # Выведет: [[1]]

root3 = None
print(s.levelOrder(root3))  # Выведет: []