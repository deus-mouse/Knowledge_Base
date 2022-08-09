

input = [2, -4, 7, 1]
# input = [1, 1, 2, 2]
# input = [35, 14, 11, -3]


import sys

input = []
for _ in range(4):
    char = int(sys.stdin.readline().strip())
    input.append(char)

a, b, c, d = input

res = set()
for x in range(100):
    if (c * x != -d) and (a * x == -b):
        res.add(x)

if res:
    [print(x) for x in res]
elif len(res) > 50:
    print('INF')
else:
    print('NO')