# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y  # Находим различия между битами с помощью XOR
        print(f'{bin(x)=}, {bin(y)=}')
        print(f'{xor=}, {bin(xor)=}')
        return bin(xor).count('1')  # Подсчитываем количество единиц в двоичном представлении








s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(3, 1))