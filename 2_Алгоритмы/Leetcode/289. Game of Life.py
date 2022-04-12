'''
https://leetcode.com/problems/game-of-life/
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''
from collections import defaultdict

board = [[1,1],[1,0]]

class Solution(object):

    def __init__(self):
        self.neighbors = list()
        self.board = None

    def neighbors_finder(self, line_index=None, cell_index=None):
        if 0 <= line_index <= len(self.board)-1 and  0 <= cell_index <= len(self.board[0])-1:
            self.neighbors.append(self.board[line_index][cell_index])

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        copy_board = board
        for line_index in range(len(board)):
            for cell_index in range(len(board[0])):
                self.lives_dict = defaultdict(int)
                self.neighbors = list()
                self.neighbors_finder(line_index-1, cell_index-1)
                self.neighbors_finder(line_index-1, cell_index)
                self.neighbors_finder(line_index-1, cell_index+1)

                self.neighbors_finder(line_index, cell_index-1)
                self.neighbors_finder(line_index, cell_index+1)

                self.neighbors_finder(line_index+1, cell_index-1)
                self.neighbors_finder(line_index+1, cell_index)
                self.neighbors_finder(line_index+1, cell_index+1)
                for char in self.neighbors:
                    self.lives_dict[char] += 1
                lives = self.lives_dict[1]

            if board[line_index][cell_index] == 1:
                if lives < 2 or lives > 3:
                    copy_board[line_index][cell_index] = 0
            else:
                if lives == 3:
                    copy_board[line_index][cell_index] = 1

            print(copy_board)
            return copy_board



sol = Solution()
sol.gameOfLife(board)