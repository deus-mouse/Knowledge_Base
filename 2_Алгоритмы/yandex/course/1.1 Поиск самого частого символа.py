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
# Переберем все позиции и для каждой позиции в строке еще раз переберем все позиции
# и в случае совпадения прибавим к счетчику единицу. Найдем максимальное значение счетчика
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
# Переберем все символы, встречающиеся в строке, а затем переберем
# все позиции и в случае совпадения прибавим к счетчику единицу.
# Найдем максимальное значение счетчика
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
# Заведем словарь, где ключом является символ, а значением — сколько
# раз он встретился. Если символ встретился впервые — создаем
# элемент словаря с ключом, совпадающем с этим символом
# и значением ноль. Прибавляем к элементу словаря с ключом,
# совпадающем с этим символом, единицу
def solved3(s):
    '''
    O(N+K) - где K количество символов БЕЗ повторений (в set()).
    "+" потому что не во вложенном цикле, а следующeм
    '''
    ans = ''
    anscnt = 0
    symcnt = {}
    for now in s:
        if now not in symcnt:
            symcnt[now] = 0
        symcnt[now] += 1

    # ищем ключ с макс значением
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