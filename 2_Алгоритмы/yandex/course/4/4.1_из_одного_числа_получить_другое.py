# Дано два числа Х и У без ведущих нулей
# Необходимо проверить, можно ли получить первое
# из второго перестановкой цифр

# Решение
# Посчитаем количество вхождений каждой цифры в каждое
# из чисел и сравним. Цифры будем постепенно добывать
# из числа справа с помощью % 10 и ll 10


def isdigitpermutation(x, y) :
    def countdigits(num):
        digitcount = [0] * 10
        while num > 0:
            lastdigit = num % 10
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    print(f'{digitsx=}')
    digitsy = countdigits(y)
    print(f'{digitsy=}')
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True


print(f'{isdigitpermutation(2021, 2012)=}')