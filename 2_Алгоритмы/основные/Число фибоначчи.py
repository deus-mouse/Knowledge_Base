# Число фибоначчи
'''
(последовательность A000045 в OEIS), в которой первые два числа равны 0 и 1,
а каждое последующее число равно сумме двух предыдущих чисел
'''
def fib():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

for i, f in zip(range(70+1), fib()):
    print('{i:3}:{f:3}'.format(i=i, f=f))


# рекусривно. НО НЕЭФФЕКТИВНО!
def recursion_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recursion_fib(n-1) + recursion_fib(n-2)

print(recursion_fib(70))