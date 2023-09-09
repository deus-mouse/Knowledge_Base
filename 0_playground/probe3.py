result = {0: 1, 1: 2, 2: 1, 3: 3, 4: 3, 5: 2}
colors = max(result.values())
print(colors)

new_result = {i: [] for i in range(1, colors+1)}
print(f'{new_result=}')

for k, v in result.items():
    new_result[v].append(k)

print(f'{new_result=}')
