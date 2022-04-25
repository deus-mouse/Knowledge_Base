'''
Дана строки в кодировке UTF-8

Найти самый часто встречающийся в ней символ.
Если несколько символов встречаются одинаково часто, то можно вывести любой.
'''

from collections import defaultdict

s = input()
ans = ''
anscnt = 0
symcnt = {}
for now in s:
    if now not in symcnt:
        symcnt[now] = 0
    symcnt[now] += 1
    if symcnt[now] > anscnt:
        ans = now
        anscnt = symcnt[now]
print(ans)



dct = defaultdict(int)

for char in s:
    dct[char] += 1

# print(dct)
# print(f'{dct.get=}')
ans = (max(dct, key=dct.get))
anscnt = dct[ans]

# print(anscnt)
print(ans)
