from collections import ChainMap


dict_1 = {x: x + x for x in range(1, 4)}
dict_2 = {x: x + x for x in range(4, 7)}

chain = ChainMap(dict_1, dict_2)
print(f'{chain=}')

print(f'{chain.get(4)=}')  # =8