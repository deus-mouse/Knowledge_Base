# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []  # Инициализация списка ответов
        for i in range(1, n + 1):  # Цикл от 1 до n включительно
            if i % 3 == 0 and i % 5 == 0:  # Если число делится и на 3, и на 5
                answer.append("FizzBuzz")
            elif i % 3 == 0:  # Если число делится только на 3
                answer.append("Fizz")
            elif i % 5 == 0:  # Если число делится только на 5
                answer.append("Buzz")
            else:  # Если число не делится ни на 3, ни на 5
                answer.append(str(i))  # Преобразование числа в строку и добавление в список
        return answer


s = Solution()
print(s.fizzBuzz(3))  # Вывод: ["1", "2", "Fizz"]
print(s.fizzBuzz(5))  # Вывод: ["1", "2", "Fizz", "4", "Buzz"]
print(s.fizzBuzz(15))  # Вывод: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
