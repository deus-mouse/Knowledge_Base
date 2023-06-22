'''
Комбинированные встроенные структуры данных

queue (очередь)
deque (двустороння очередь)
defaultdict (словарь с указанием типа элемента по умолчанию)
namedtuple (сместь списка и словаря)
'''

class FIFO:  # очередь
    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(0)  # pop() заберет последний


fifo = FIFO()
fifo.put(1)
fifo.put(2)
print(f'{fifo.get()=}')
print(f'{fifo.get()=}')


# двусвязная очередь
from collections import deque

my_deque = deque([1, 2, 3])
my_deque.appendleft(5)
print(f'{my_deque=}')
my_deque.append(5)
print(f'{my_deque=}')

my_deque.popleft()
my_deque.pop()
print(f'{my_deque=}')



