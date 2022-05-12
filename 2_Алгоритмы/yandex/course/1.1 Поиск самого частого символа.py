'''
Дана строки в кодировке UTF-8

Найти самый часто встречающийся в ней символ.
Если несколько символов встречаются одинаково часто, то можно вывести любой.
'''

from collections import defaultdict

s = input()

# решение в одну строку
def solved(s):
    return max(map(lambda x: (s.count(x), x), s))[1]


# Решение № 1
def solved1(s):
    '''
    O(n2)
    '''
    ans = ''
    anscnt = 0
    for i in range(len(s)):  # берем индекс по порядку
        nowcnt = 0
        for j in range(len(s)):  # перебираем все индексы и сравниваем с первым
            if s[i] == s[j]:
                nowcnt += 1
        if nowcnt > anscnt:  # перебрав каждый круг мы обновляемя значения
            ans = s[i]
            anscnt = nowcnt
    return ans


# Решение № 2
def solved2(s):
    '''
    O(NK) - где K количество символов БЕЗ повторений (в set())
    '''
    ans = ''
    anscnt = 0
    for now in set(s):  # берем индекс по порядку
        nowcnt = 0
        for j in range(len(s)):  # перебираем все индексы и сравниваем с первым
            if now == s[j]:
                nowcnt += 1
        if nowcnt > anscnt:  # перебрав каждый круг мы обновляемя значения
            ans = now
            anscnt = nowcnt
    return ans


# Решение № 3
def solved3(s):
    '''
    O(N+K) - где K количество символов БЕЗ повторений (в set()).
    "+" потому что не во вложенном цикле, а следующим
    '''
    ans = ''
    anscnt = 0
    symcnt = {}
    for now in s:
        if now not in symcnt:
            symcnt[now] = 0
        symcnt[now] += 1

    for key in symcnt:
        if symcnt[key] > anscnt:
            anscnt = symcnt[key]
            ans = key

    return ans


# Решение № 3 (Модифицированное)
def solved4(s):
    '''
    O(N+K) - где K количество символов БЕЗ повторений (в set()).
    "+" потому что не во вложенном цикле, а следующим
    '''
    ans = ''  # !! если не определить, то передав на вход ПУСТУЮ строку, мы не зайдем в цикл и не определим ее ниже в цикле, нечего будет вернуть
    anscnt = 0
    symcnt = {}
    for now in s:
        if now not in symcnt:
            symcnt[now] = 0
        symcnt[now] += 1
        if symcnt[now] > anscnt:
            ans = now
            anscnt = symcnt[now]
    return ans


# Решение № 5 MY
def my_solved(s):
    dct = defaultdict(int)

    for char in s:
        dct[char] += 1

    # print(dct)
    # print(f'{dct.get=}')
    ans = (max(dct, key=dct.get))
    anscnt = dct[ans]
    # print(anscnt)
    return ans


print(f'{solved3(s)=}')
print(f'{solved4(s)=}')
print(f'{my_solved(s)=}')