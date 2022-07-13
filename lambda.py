s = [
    'fgs432gs sadfs43f 12',
    'fgsg4s sadfs13f 14',
    'fgsg43s sadf1sf 54',
    'fgsg12s sadfsf 15',
    'fgsgs sadf2sf 1546',
    'fgsg4s sadfs234 1',
]

s.sort(key = (lambda x: x.split(" ")[-1]))

print(s)


l = lambda s: s[0] if s else None

print(f'{s=}')