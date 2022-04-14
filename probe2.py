
from collections import defaultdict
from copy import deepcopy


class Solution(object):

    def __init__(self):
        self.board = None

    def neighbors_finder(self, line_index=None, cell_index=None):
        if (0 <= line_index <= len(self.board)-1) and (0 <= cell_index <= len(self.board[0])-1):
            self.neighbors.append(self.board[line_index][cell_index])

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        copy_board = deepcopy(board)
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

        return copy_board



sol = Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
