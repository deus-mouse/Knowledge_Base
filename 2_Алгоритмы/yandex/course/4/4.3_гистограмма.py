# Дана строка S
# Выведите гистограмму как в примере (коды символов отсортированы)

# Мое решение:

S = 'Hello, world!'

def_dict_int = {}


def dict_filler(d: dict, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


def gistogramm_painter(s):
    for symbol in s:
        dict_filler(def_dict_int, symbol)


gistogramm_painter(S)
set_s = sorted(set(S))
rows = []

while True:
    is_empty = True
    row = list()
    for key in set_s:
        if def_dict_int[key] > 0:
            is_empty = False
            row.append('#')
            def_dict_int[key] -= 1
        else:
            row.append(' ')
    rows.append(row)
    if is_empty:
        break

for row in reversed(rows):
    print(''.join(row))


# Его решение
def printchart(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])  # нашли максимум
    sorteduniqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorteduniqsyms))


printchart(S)