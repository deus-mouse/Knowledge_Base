# Дана последовательность слов
# Вывести все самые короткие слова через пробел.

from math import inf

words = ['Дан', 'последовательность', 'слов', 'Вывести', 'все', 'самые',
        'короткие', 'слова', 'через', 'пробел', ]

def foo1(words):
    min = inf
    result = ''
    for word in words:
        if min > len(word):
            min = len(word)
            result = word
        elif min == len(word):
            result += f' {word}'  # Очень долго! строка НЕизменяемый объект. каждый раз происходит копирование
    return print(f'1 -> {result=}')

foo1(words)


# Решение его
def short_words(words):
    minlen= len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)  # нашли длинну самого короткого слова
    ans = []  # добавление в список это быстрая операция O(n)
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)

print(short_words(words))


# Мое + его решение
def foo2(words):
    min = inf
    result = []
    for word in words:
        if min > len(word):
            min = len(word)
            result = [word]
        elif min == len(word):
            result.append(word)
    return print(f'2 -> {" ".join(result)=}')

foo2(words)
