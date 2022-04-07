'''
G. Интересное путешествие

Не секрет, что некоторые программисты очень любят путешествовать.
Хорошо всем известный программист Петя тоже очень любит путешествовать,
посещать музеи и осматривать достопримечательности других городов.
Для перемещений между из города в город он предпочитает использовать машину.
При этом он заправляется только на станциях в городах, но не на станциях по пути.
Поэтому он очень аккуратно выбирает маршруты, чтобы машина не заглохла в дороге.
А ещё Петя очень важный член команды, поэтому он не может себе позволить путешествовать слишком долго.
Он решил написать программу, которая поможет ему с выбором очередного путешествия.
Но так как сейчас у него слишком много других задач, он попросил вас помочь ему.
Расстояние между двумя городами считается как сумма модулей разности по каждой из координат.
Дороги есть между всеми парами городов.

Формат ввода
В первой строке входных данных записано количество городов n. 

В следующих n строках даны два целых числа: координаты каждого города, не превосходящие по модулю миллиарда. 
Все города пронумерованы числами от 1 до n в порядке записи во входных данных.

В следующей строке записано целое положительное число k, не превосходящее двух миллиардов, 
— максимальное расстояние между городами, которое Петя может преодолеть без дозаправки машины.

В последней строке записаны два различных числа — номер города, откуда едет Петя, и номер города, куда он едет.

Формат вывода
Если существуют пути, удовлетворяющие описанным выше условиям, то выведите минимальное количество дорог, 
которое нужно проехать, чтобы попасть из начальной точки маршрута в конечную. Если пути не существует, выведите -1.
'''

# Также можно решить через Матрицу смежности
# https://www.youtube.com/watch?v=MCfjc_UIP1M
# создаем матрицу
# matrix = list()
# for line in range(N):
#     matrix.append([])
#     a = geo[line + 1]
#     for column in range(N):
#         b = geo[column + 1]
#         ab = distance(a, b)
#         if ab:
#             matrix[line].append(1)
#         else:
#             matrix[line].append(0)
#
# for line in matrix:
#     print(f'{line=}')


import sys
from collections import deque  # применим структуру данных очередь
# обладает доп методами не усложняющими вычисление = O(1)
# appendleft() - добавляет элемент в начало списка
# popleft() - удаляет элемент из начало списка


# общая функция определения расстояния между городами
def distance(a, b):
    ab = ((b[0] - a[0])**2 + (b[1] - a[1])**2) ** (0.5)
    if ab <= k:
        return True
    else:
        return False


####################################################################################
# 1-й способ (РАБОЧИЙ до 19 теста)
# https://www.youtube.com/watch?v=S-hjsamsK8U

# определение окружения
N = int(sys.stdin.readline().strip())

geo2 = dict()  # словарь городов с их координатами
for n in range(N):  # >>> geo2={0: [0, 0], 1: [2, 0], 2: [0, 2], 3: [2, 2]}
    a, b = sys.stdin.readline().strip().split(' ')
    geo2[n] = [int(a), int(b)]

k = int(sys.stdin.readline().strip())  # расстояние которое может пройти за один раз
points = sys.stdin.readline().strip().split(' ')
start = int(points[0])-1
finish = int(points[1])-1

# создаем граф
graph2 = dict()
for city_a in range(len(geo2)):  # >>> graph2={0: {1, 2}, 1: {0, 3}, 2: {0, 3}, 3: {1, 2}}
    graph2[city_a] = set()
    a = geo2[city_a]
    for city_b in range(len(geo2)):
        if city_a == city_b:
            continue
        b = geo2[city_b]
        ab = distance(a, b)
        if ab:
            graph2[city_a].add(city_b)

distances = [None] * N  # массив расстояний, по умолчанию неизвестны
# >>> [None, None, None, None]
start_vertex = start  # стартовая вершина, начинаем с нее
distances[start_vertex] = 0  # расстояние до себя же равно 0 
# >>> [None, 0, None, None]
queue = deque([start_vertex])  # создаем очередь 
# >>> deque([1])


# поиск в ширину Breadth-first search
while queue:  # пока очередь не пуста
    cur_v = queue.popleft()  # достаем 1-ый элемент
    for neigh_v in graph2[cur_v]:  # проходим всех его соседей
        if distances[neigh_v] is None:  # если сосед еще НЕ посещен (=> расстояние None)
            distances[neigh_v] = distances[cur_v] + 1  # считаем расстояние
            queue.append(neigh_v)  # добавляем в очередь, чтобы проверить и его соседей

print(distances[finish] if distances[finish] else -1)


####################################################################################
# 2-й способ. (НE работает)
# определение окружения
# N = int(sys.stdin.readline().strip())
# 
# geo1 = dict()  # нумерация от 1-цы
# for n in range(1, N + 1):
#     a, b = sys.stdin.readline().strip().split(' ')
#     geo1[n] = [int(a), int(b)]
# # >>> geo1={1: [0, 0], 2: [2, 0], 3: [0, 2], 4: [2, 2]}
# 
# k = int(sys.stdin.readline().strip())
# points = sys.stdin.readline().strip().split(' ')
# start = int(points[0])
# finish = int(points[1])
# 
# 
# # создаем невзвешанный граф
# graph1 = dict()
# for line in range(N):
#     graph1[line+1] = set()  # используем множества для скорости
#     a = geo1[line + 1]
#     for column in range(N):
#         b = geo1[column + 1]
#         ab = distance(a, b)
#         if ab:  # если может добраться, то ставим ребро
#             graph1[line+1].add(column+1)
# # >>> graph1={1: {1, 2}, 2: {0, 3}, 3: {0, 3}, 4: {1, 2}}
# 
# 
# # поиск в ширину Breadth-first search
# def bfs(start, finish, graph):
#     search_queue = deque()
#     search_queue += graph[start]
#     visited = []
#     steps = []
#     step = 0
#     while search_queue:
#         node = search_queue.popleft()
#         if not node in visited:
#             if node == finish:
#                 print('FOUND')
#                 steps.append(step)
#                 step = 0
#                 # return True
#             else:
#                 search_queue += graph[node]
#                 visited += [node]
#                 step += 1
#     print('NOT FOUND')
#     print(f'{steps=}')
#     # return False
# 
# # bfs(start, finish, graph1)


