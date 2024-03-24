# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

# lib = {1: 'I',
#        5: 'V',
#        10: 'X',
#        50: 'L',
#        100: 'C',
#        500: 'D',
#        1000: 'M'}
lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

short_list = {'I': {4: 'IV', 9: 'IX'},
              'X': {4: 'XL', 9: 'XC'},
              'C': {4: 'CD', 9: 'CM'}}

class Solution:
    def romanToInt(self, s: str) -> int:
        # Словарь для соответствия римских цифр и их значений
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0  # Итоговое число
        prev = 0  # Значение предыдущей римской цифры

        for i in reversed(s):  # Проходим строку справа налево
            print(f'{i=}')
            print(f'{roman[i]=}, {prev=}')

            if roman[i] < prev:
                total -= roman[i]  # Вычитаем, если предыдущее больше текущего
            else:
                total += roman[i]  # Иначе добавляем
            print(f'{total=}')
            prev = roman[i]  # Обновляем предыдущее значение
            print('=========')
        return total


    def intToRoman(self, s: int) -> int:
        dd = {}  # {'M': 2, ...}

        for k, v in reversed(lib.items()):
            print(f'{k=}, {v=}')
            res = s // lib[k]
            print(f'{res=}')
            if k in ('C', 'X', 'I'):
                if res in (4, 9):
                    k = short_list[k][res]
                    dd[k] = 1
                else:
                    dd[k] = res
            else:
                dd[k] = res
            print(f'{dd=}')
            s -= res * v
            print(f'{s=}')
            print('=========')
        print(f'{dd=}')

        S = ''.join([i*dd[i] for i in dd])
        return S



s = Solution()
r = "LVIII"  # 58
r = 58  # "LVIII"
r = 1994  # "MCMXCIV"
# print(s.intToRoman(r))
r = "LVIII"  # 58
r = "MCMXCIV"  # 58
print(s.romanToInt(r))