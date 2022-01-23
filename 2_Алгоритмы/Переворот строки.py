# Переворот строки

some_string = 'Neuronet Neuronet'

def reverse_string(s):
    chars = list(s)  # разбираем строку на символы

    for i in range(len(s) // 2):
        # до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)

print(some_string)
print(reverse_string(some_string))

# Самый быстрый и легкий способ в Python
print(some_string[::-1])


