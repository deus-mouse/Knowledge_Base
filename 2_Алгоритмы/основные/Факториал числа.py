# Факториал числа
#  5 ! = 1 * 2 * 3 * 4 * 5 = 120.
number = 5
def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 0
    while i < n:
        i += 1
        f = f * i
        print(f)
    return f
print(factorial(number))


# Используя рекурсию
def recursion_factorial(n):
    if n == 1:
        return 1
    return recursion_factorial(n-1) * n

print(recursion_factorial(4))