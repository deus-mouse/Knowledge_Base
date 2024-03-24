# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/

'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation,
as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0  # Начинаем с нуля
        for i in range(32):  # Для каждого из 32 битов
            print(f'{n >> i = }')

            bit = (n >> i) & 1  # Получаем i-тый бит, сдвигая n вправо на i позиций и применяя побитовый AND с 1
            print(f'{bit=}')
            result = result | (bit << (31 - i))  # Сдвигаем бит влево на (31-i) позиций и добавляем его к результату через OR
            print(f'{result=}')

        return result


# >> и << - операторы сдвига вправо и влево, соответственно, которые используются для перемещения битов.
# & - побитовый AND, используемый для извлечения конкретного бита.
# | - побитовый OR, используемый для добавления бита в результат.

# Big O анализ эффективности:
# Временная сложность:
# O(1) - алгоритм всегда проходит через 32 итерации, независимо от размера входных данных, так как работает с 32-битными числами.
# Пространственная сложность:
# O(1) - использует константное количество памяти, не зависящее от входных данных.




s = Solution()
# Пример 1
n1 = 0b00000010100101000001111010011100
print(f"Original: {bin(n1)}")
print(f"Reversed: {bin(s.reverseBits(n1))}")

# Пример 2
n2 = 0b11111111111111111111111111111101
print(f"Original: {bin(n2)}")
print(f"Reversed: {bin(s.reverseBits(n2))}")