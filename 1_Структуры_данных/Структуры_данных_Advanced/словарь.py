'''
https://www.youtube.com/watch?v=bClOG0X6bWo
list - список
dict - словарь
set - множество
tuple - кортеж
'''

my_defualt_dict = {'a': 1, 'b': 2}
# print(my_defualt_dict['c'])  # KeyError: 'c'
print(my_defualt_dict.get('c'))  # None


class MyDict(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        return -1


mydict2 = MyDict(my_defualt_dict)
print(mydict2['c'])  # -1
print(my_defualt_dict.get('c', -1))  # тоже самое


# как из словаря получать данные по индексу
# print(f'{mydict.items()[1]=}')  # TypeError: 'dict_items' object is not subscriptable
print(f'{list(my_defualt_dict.items())[1]=}')  # преобразовав в список получится

# а если классом
class IndexDict(dict):
    def __getitem__(self, key):
        if isinstance(key, int):
            return list(my_defualt_dict.items())[key]
        else:
            return super().__getitem__(key)

mydict3 = IndexDict(my_defualt_dict)
print(f'{mydict3[1]=}')  # ('b', 2)
print(f'{mydict3["a"]=}')  # 1


# поиск по вложенному словарю
my_defualt_dict2 = {
    'Users': [
        {'Name': 'Roman',
         'Interests': [
             {'Id': 555,
              'name': 'FPV'}
         ]}
    ],
    'Items': [

    ]
}

print(f"{my_defualt_dict2['Users'][0]['Interests'][0]['Id']=}")

# а если не будет такого значения, то выпадет ошибка.
# как это обработать?

my_defualt_dict3 = {
    'Users': [
        {'Name': 'Roman'}
    ],
    'Items': [
    ]
}

# print(f"{my_defualt_dict3['Users'][0]['Interests'][0]['Id']=}")  # KeyError: 'Interests'
print(f"{my_defualt_dict3.get('Users', [{}])[0].get('Interests', [{}])[0].get('Id', -1)=}")  # -1
print(f"{my_defualt_dict2.get('Users', [{}])[0].get('Interests', [{}])[0].get('Id', -1)=}")  # 555

