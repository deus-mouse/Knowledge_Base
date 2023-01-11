'''
Данная реализация очереди с приоритетом во внутреннем представлении
использует двоичную кучу heapq и имеет одинаковую временную и про-
странственную вычислительную сложность2.

Разница состоит в том, что очередь с приоритетом PriorityQueue синхро-
низирована и обеспечивает семантику блокирования с целью поддержки
многочисленных параллельных производителей и потребителей.

Реализация queue.PriorityQueue выбивается из общего ряда, отлича-
ясь хорошим объектно-ориентированным интерфейсом и именем, ко-
торое четко указывает на ее направленность. Такая реализация должна
быть предпочтительным вариантом.
'''

from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'программировать'))
q.put((1, 'есть'))
q.put((3, 'спать'))

while not q.empty():
    next_item = q.get()
    print(next_item)
# Результат:
# (1, 'есть')
# (2, 'программировать')
# (3, 'спать')