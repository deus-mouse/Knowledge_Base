# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from typing import List

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],

         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],

         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # True


class Solution:
    def isValidSudoku_gpt(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]

                box_index = (r // 3) * 3 + c // 3
                '''
Формула (r // 3) * 3 + c // 3 используется для определения индекса подквадрата 3x3 на доске Судоку. Давайте разберем, как она работает, на примере доски Судоку размером 9x9.
Доска делится на 9 подквадратов 3x3, индексируемых от 0 до 8:
[0][1][2]
[3][4][5]
[6][7][8]
r обозначает индекс строки текущей ячейки.
c обозначает индекс столбца текущей ячейки.
Операция // обозначает целочисленное деление, которое делит числа, отбрасывая дробную часть.
Почему (r // 3) и (c // 3)?
r // 3 делит доску на горизонтальные сегменты (ряды подквадратов). Это превращает индекс строки в номер горизонтальной группы подквадратов 3x3 (0 для строк 0-2, 1 для строк 3-5, 2 для строк 6-8).
c // 3 делит доску на вертикальные сегменты (колонки подквадратов). Это превращает индекс столбца в номер вертикальной группы подквадратов 3x3 (0 для столбцов 0-2, 1 для столбцов 3-5, 2 для столбцов 6-8).
Как получается индекс подквадрата?
Умножая (r // 3) на 3, мы получаем начало каждой горизонтальной группы подквадратов в индексации подквадратов. Это 0, 3 и 6 для первой, второй и третьей горизонтальных групп соответственно.
Прибавляя к этому (c // 3), мы сдвигаемся вправо в пределах группы, чтобы выбрать конкретный подквадрат. Это добавляет 0, 1 или 2 в зависимости от того, в каком столбце находится ячейка.
                '''

                if (num in rows[r]) or (num in cols[c]) or (num in boxes[box_index]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for row in board:
            figures = [num for num in row if num != '.']
            rows = len(figures) == len(set(figures))
            if not rows:
                return rows

        # columns
        for i in range(0, len(board[0])):
            column = [row[i] for row in board]  #  разворот. Транспонирование матрицы
            figures = [num for num in column if num != '.']
            columns = len(figures) == len(set(figures))
            if not columns:
                return columns

        # squares
        width = 3
        line_groups = []
        for row in range(0, len(board), width):
            line_groups.append(board[row:row+width])

        square = []
        for group in line_groups:  # group: [[], [], []]
            for i in range(0, len(group[0])):
                column = [row[i] for row in group]  # переворачиваем. Транспонирование матрицы
                square.extend(column)
                if len(square) == width * width:
                    figures = [num for num in square if num != '.']
                    diff = len(figures) != len(set(figures))
                    if diff:
                        return False
                    square = []

        return True


s = Solution()
# print(s.isValidSudoku(board))
print(s.isValidSudoku_gpt(board))
