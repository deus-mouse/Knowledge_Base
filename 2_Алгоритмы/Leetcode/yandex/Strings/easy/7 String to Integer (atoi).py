# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''

# s = "42"  # 42
# s = "   -42"  # -42
# s = "4193 with words"
# s = "words and 987"
# s = "words and"
# s = "3.14159"
# s = ".1"
s = "+-12"  # 0


class Solution:
    def myAtoi_GPT(self, s: str) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Step 1: Ignore leading whitespaces
        s = s.lstrip()

        # Step 2: Check if the next character is '-' or '+'
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        # Step 3: Read in next the characters until the next non-digit character
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)  # (сдвигаем его на один разряд влево) и добавляем к нему новую цифру. Это соответствует прибавлению цифры на соответствующем месте в числе.
            else:
                break

        # Apply the sign
        result *= sign

        # Step 5: Clamp the integer to remain in the 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

    def myAtoi2(self, s: str) -> int:
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1
        s = s.replace(' ', '')
        s2: str = '0'
        sign: int = 0

        for i, char in enumerate(s):
            if char.isalpha() or char == '.':
                break
            if char == '-' and s[i+1].isdigit():
                sign = -1
            elif char.isdigit():
                s2 = ''.join([s2, char])
                if not sign:
                    if i > 0:
                        sign = -1 if s[i-1] == '-' else 1
                    else:
                        sign = 1
            elif sign:
                break

        s2 = int(s2) * sign

        if s2 < int_min:
            return int_min
        elif s2 > int_max:
            return int_max
        else:
            return s2

    def myAtoi1(self, s: str) -> int:
        # читает цифры во всей строке, а нужно только вначале
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1
        s2 = '0'
        sign = 0
        for i, char in enumerate(s):
            if char.isdigit():
                s2 = ''.join([s2, char])
                if not sign and i > 0:
                    sign = -1 if s[i-1] == '-' else 1
            elif sign:
                break

        s2 = int(s2) * sign

        if s2 < int_min:
            return int_min
        elif s2 > int_max:
            return int_max
        else:
            return s2


res = Solution()
print(res.myAtoi_GPT(s))
