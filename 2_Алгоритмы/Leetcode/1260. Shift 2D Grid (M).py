'''
https://leetcode.com/problems/shift-2d-grid/
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
'''

from collections import deque

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4


class Solution(object):
    def shiftGrid(self, grid, k):

        # превращаем в очереди
        for l in range(len(grid)):
            grid[l] = deque(grid[l])

        m = len(grid)
        n = len(grid[0])

        while k:
            for line in range(m):
                if line == m-1:
                    grid[0].appendleft(grid[line].pop())
                else:
                    grid[line+1].appendleft(grid[line].pop())

            k -= 1

        return grid


result = Solution()
result.shiftGrid(grid, k)