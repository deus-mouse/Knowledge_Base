from collections import defaultdict


standart_dict = dict(one=1, two=2, three=3)
print(f'{standart_dict=}')


defdict_1 = defaultdict(list)
defdict_1['data'].append(1)
defdict_1['data'].append(2)
defdict_1['data'].append(3)

print(f'{defdict_1=}')
print(f'{defdict_1["undefind_key"]=}')  # []


defdict_2 = defaultdict(dict)
defdict_2['data'] = {'one': 1}
print(f"{defdict_2['data'].keys()=}")

print(f'{defdict_2=}')
print(f'{defdict_2["undefind_key"]=}')  # {}


defdict_3 = defaultdict(str)
defdict_3['data'] = 2

print(f'{defdict_3=}')
print(f'{defdict_3["undefind_key"]=}')  # ''