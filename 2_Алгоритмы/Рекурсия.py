# https://www.youtube.com/watch?v=jvFULnNpNLg

def rec(x):
    if x < 4:
        print(x)
        rec(x+1)
        print(x)

rec(1)

# 1
# 2
# 3
# 3
# 2
# 1
# Функция вызывает сама себя и а потом по ступеням возвращается к первому вызову


# палиндром
# шалаш
# asdffdsa
# "", "a"

def is_palindrom(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrom(s[1:-1])

print(is_palindrom("шалаш"))