# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:  # Если число строк равно 0, возвращаем пустой список
            return []

        triangle = [[1]]  # Инициализируем треугольник первой строкой

        for i in range(1, numRows):
            row = [1]  # Первый элемент строки всегда 1
            # Каждый элемент внутри строки - это сумма двух элементов над ним из предыдущей строки
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Последний элемент строки всегда 1
            triangle.append(row)  # Добавляем построенную строку в треугольник

        return triangle



# Анализ Big O эффективности:
# Временная сложность:
# O(numRows2) - потому что для каждой из numRows строк мы выполняем итерации,
# количество которых пропорционально номеру строки.
# Сумма длин всех строк даёт арифметическую прогрессию,
# сумма которой пропорциональна квадрату числа строк.

# Пространственная сложность:
# O(numRows2) - поскольку мы сохраняем все предыдущие строки для генерации следующих,
# общее количество элементов во всех строках также будет пропорционально квадрату числа строк.



s = Solution()
print(s.generate(5))
# Вывод: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print(s.generate(1))
# Вывод: [[1]]