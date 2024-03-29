'''
Класс deque реализует очередь с двусторонним доступом, которая под-
держивает добавление и удаление элементов с любого конца за O(1)
(неамортизируемое) время. Поскольку двусторонние очереди одинаково
хорошо поддерживают добавление и удаление элементов с любого конца,
они могут служить и в качестве очередей, и в качестве стеков1.
Объекты Python deque реализованы как двунаправленные связные спи-
ски, что дает им стабильную производительность для операций вставки
и удаления элементов, но при этом плохую O(n) производительность для
произвольного доступа к элементам в середине очереди2.
'''


from collections import deque

s = deque()
s.append('есть')
s.append('спать')
s.append('программировать')
print(s)
# deque(['есть', 'спать', 'программировать'])

s.pop()
# 'программировать'
s.pop()
# 'спать'
s.pop()
# 'есть'
s.pop()
# IndexError: "pop from an empty deque"