n = 6
adjList = [[] for _ in range(n)]

edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

for (src, dest) in edges:
    print(f'{src=}, {dest=}')
    adjList[src].append(dest)
    adjList[dest].append(src)
    print(f'{adjList=}')


for u in range(n):
    print(f'{u=}')


s = set([1, 1, 2])
print(f'{s=}')