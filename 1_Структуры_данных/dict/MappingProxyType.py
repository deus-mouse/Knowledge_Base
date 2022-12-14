from types import MappingProxyType


writable = {x: x + x for x in range(1, 4)}

read_only = MappingProxyType(writable)
# read_only[1] = 100
print(f'{read_only=}')

writable[1] = 100
print(f'{writable=}')

print(f'{read_only=}')