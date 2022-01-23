# список
# кортеж
# словарь
# множество


# Список

list.append()
list.insert(0, ‘something’)
list.extend([list]) # добавление списка в список
list.remove(x) # Удалите из списка первый элемент, значение которого равно x
list.pop() # удаление с возвратом
list.reverse()
list.sort() # сортирует, изменяя сам список
list.sorted() # сортирует, не изменяя сам список возвращая другой
del list[<index>] # удаление по индексу
list.count( х ) # Возвращает количество раз, когда x появляется в списке.
list.clear( ) # Удалите все элементы из списка. Эквивалентно .del a[:]


# Словарь
ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
     }

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])




# Последовательности

# Основные возможности – это проверка принадлежности
# (т.е. выражения “in” и “not in”) и оператор индексирования,
# позволяющий получить напрямую некоторый элемент последовательности.

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])





# Множество

# – это неупорядоченные наборы простых объектов.
# Они необходимы тогда, когда присутствие объекта в наборе важнее порядка или того,
# сколько раз данный объект там встречается.

>>> bri = set(['Бразилия', 'Россия', 'Индия'])
>>> 'Индия' in bri
True
>>> 'США' in bri
False
>>> bric = bri.copy()
>>> bric.add('Китай')
>>> bric.issuperset(bri)
True
>>> bri.remove('Россия')
>>> bri & bric # OR bri.intersection(bric)
{'Бразилия', 'Индия'}





# Ссылки

print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные





# Ещё о строках
name = 'Swaroop' # Это объект строки

if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')

if 'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))
