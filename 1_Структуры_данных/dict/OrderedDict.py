
from collections import OrderedDict


standart_dict = dict(one=1, two=2, three=3)
standart_dict['four'] = 4

order = OrderedDict(one=1, two=2, three=3)
order['four'] = 4

print(f'{standart_dict=}')
print(f'{order=}')

order['two'] = 2
print(f'{order=}')