# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
from typing import List


lib = {')': '(',
       '}': '{',
       ']': '['
       }

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == lib.get(s[i]):
                del stack[-1]
            else:
                stack.append(s[i])

        return True if not stack else False

    def isValid_GPT(self, s: str) -> bool:
        # Словарь для соответствия закрывающих и открывающих скобок
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []  # Стек для отслеживания открытых скобок

        for char in s:
            if char in bracket_map:
                # Если стек пуст или верхний элемент стека не соответствует открывающей скобке
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Удаляем последнюю открытую скобку из стека
            else:
                stack.append(char)  # Добавляем открытую скобку в стек

        # Если стек пуст, все скобки корректно закрыты
        return not stack




s = Solution()
print(s.isValid('()[]{}'))

