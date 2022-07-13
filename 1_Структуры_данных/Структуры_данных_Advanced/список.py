'''
https://www.youtube.com/watch?v=bClOG0X6bWo
list - список
dict - словарь
set - множество
tuple - кортеж
'''

mylist = [1, 2, 3]  # [1, 2, 3]


# print(f'{mylist[100]}')  # IndexError: list index out of range

class MyList(list):
    def __getitem__(self, key):
        if key >= len(self):
            return 'No such index'
        return super(MyList, self).__getitem__(key)

    def __setitem__(self, key, value):
        if key >= len(self):
            self.append(value)
        else:
            super(MyList, self).__setitem__(key, value)


mylist2 = MyList(mylist)
mylist2.append(4)
print(f'{mylist2=}')
print(f'{type(mylist2)=}')
print(f'{mylist2[100]=}')  # No such index (without error)

mylist3 = MyList(mylist)
mylist3[0] = 10
print(f'{mylist3=}')
mylist3[100] = 10
# если добавим к несуществующему, то благодаря переопределенному маг. методу __setitem__
# мы положим его в конец
print(f'{mylist3=}')


# В Python динамическая типизация, т.е.  в списке могут быть разные типы данных
# mylist = [1, True, 'str', [12, 2] ...]
# сделаем список который принимает только один тип

class TypedList(list):
    def __init__(self, iterable_obj=None, data_type=None):
        super().__init__(iterable_obj)
        self.data_type = data_type
        if not self.data_type and iterable_obj:
            self.data_type = type(iterable_obj[0])  #  если тип не задан, то задаем тип первого элемента списка
        for value in iterable_obj:
            if not isinstance(value, self.data_type):
                raise ValueError('Only one type needed')

    def append(self, val) -> None:
        if not isinstance(val, self.data_type):
            raise ValueError('Only one type needed')
        super(TypedList, self).append(val)


mylist3 = TypedList(mylist)
mylist3.append(4)
print(f'{mylist3=}')
# mylist3.append('5')  # ValueError: Only one type needed



# Как преобразовать список списков в список чисел
a = [[1], [2], [3]]
lst = [x for l in a for x in l]