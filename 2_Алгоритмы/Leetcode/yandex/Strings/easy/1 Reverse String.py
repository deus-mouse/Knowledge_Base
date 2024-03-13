# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List

s = ["h","e","l","l","o"]  # ["o","l","l","e","h"]
s = ["H","a","n","n","a","h"]  # ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

    def reverseString_gpt(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            # Меняем местами символы
            s[left], s[right] = s[right], s[left]
            # Сдвигаем указатели
            left, right = left + 1, right - 1

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]  # создает новый объект в памяти!!




res = Solution()
print(res.reverseString(s))
print(f'{s=}')
