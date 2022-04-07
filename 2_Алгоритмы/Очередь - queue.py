from collections import deque  # применим структуру данных очередь
# обладает доп методами не усложняющими вычисление = O(1)
# appendleft() - добавляет элемент в начало списка
# popleft() - удаляет элемент из начало списка

q = deque()
q.append(11)
q.append(22)
q.append(33)
q.appendleft(0)
q.popleft()

print(f'{q=}')