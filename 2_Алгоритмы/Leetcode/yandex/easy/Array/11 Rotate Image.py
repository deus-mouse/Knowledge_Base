# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''
from typing import List

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]  # [[7,4,1],[8,5,2],[9,6,3]]


class Solution:
    def rotate_gpt(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(f'Transpose {matrix=}')

        # Flip the matrix horizontally
        for i in range(n):
            for j in range(n // 2):  # используется для обхода только первой половины каждой строки матрицы
                # 'n - 1' — это индекс последнего элемента в строке, поскольку индексация начинается с 0
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]  # меняются местами
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Flip the matrix horizontally
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]

        return matrix


s = Solution()
# print(s.rotate_gpt(matrix))
print(s.rotate(matrix))
