top_index = 4
island = [3, 1, 4, 3, 5, 1, 1, 3, 1]
a = len(island)

print(f'{a=}')

for index in reversed(range(top_index, len(island))):
    print(f'{index=}')
    print(f'{island[index]=}')

