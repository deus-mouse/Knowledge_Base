# Алгоритм Евклида

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

print("НОД чисел 30, 18 = ", gcd(30, 18))

# ИЛИ
import math

i = math.gcd(30, 18)
print(i)