# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

s = "A man, a plan, a canal: Panama"  # True amanaplanacanalpanama

s = "race a car"  # False

# s = 'a'

class Solution:
    def isPalindrome_GPT(self, s: str) -> bool:
        # Преобразование строки: приведение к нижнему регистру и удаление не-алфавитно-цифровых символов
        filtered_chars = ''.join(char.lower() for char in s if char.isalnum())
        # Проверка, является ли строка палиндромом
        return filtered_chars == filtered_chars[::-1]

    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join([char for char in s if char.isalpha()])
        s2 = s2.lower()

        half = len(s2) // 2

        left = s2[:half]
        right = s2[-half:]

        return left == right[::-1]



res = Solution()
print(res.isPalindrome_GPT(s))
