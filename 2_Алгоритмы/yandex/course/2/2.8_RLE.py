# дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28. И сгенерирует ошибку, если на вход
# пришла невалидная строка.

# Пояснения: Если символ встречается 1 раз, он остается без
# изменений; Если символ повторяется более 1 раза, к нему
# добавляется количество повторений.

from collections import defaultdict

data = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBB'


def rle(data):
    if not data:
        return None
    # d = defaultdict(int)
    # for letter in data:
    #     d[letter] += 1
    # return sorted(d.items())

    l = [data[0], ]
    counter = 1

    # for index in range(1, len(data)):
    #     if data[index] == data[index-1]:
    #         counter += 1
    #     else:
    #         l.append(data[index - 1])
    #         if counter > 1:
    #             l.append(str(counter))
    #         counter = 1
    # возникнет проблема в конце

    for letter in data[1:]:
        if l[-1] != letter:
            if counter > 1:
                l.append(str(counter))
            l.append(letter)
            counter = 1
        elif letter == l[-1]:
            counter += 1
    l.append(str(counter))

    return "".join(l)


print(f'{rle(data)=}')


# его решение. по сути тоже самое, только он не счетчик открывает, а считает разницу между открывающим индексом и закрывающим
# т.е. гже началась последовательность и где закончилась

def rle2(s):
    def pack(s, cnt):
        # упаковывает символ + счетчик
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(1, len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)

print(f'{rle2(data)=}')
