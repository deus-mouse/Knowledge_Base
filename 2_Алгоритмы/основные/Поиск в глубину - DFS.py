'''
Алгоритм DFS
https://evileg.com/ru/post/494/#header_DFS_%D0%B2_Python
Стандартная реализация DFS помещает каждую вершину графа в одну из двух категорий:
Посещенные.
Не посещенные.

Цель алгоритма - пометить каждую вершину, как посещенную, избегая циклов.

Алгоритм DFS работает следующим образом:

Начните с размещения любой вершины графа на вершине стека.
Возьмите верхний элемент стека и добавьте его в список посещенных.
Создайте список смежных узлов этой вершины. Добавьте те, которых нет в списке посещенных, в начало стека.
Продолжайте повторять шаги 2 и 3, пока стек не станет пустым.
'''


graph = {
    0: {1, 2, 3},
    1: {0, 2},
    2: {0, 1, 4},
    3: {0},
    4: {2},
}


def dfs(graph, start, visited=None):

    if start == 3:
        print('FOUND')

    if visited is None:
        visited = set()

    visited.add(start)

    print(f'{start=}')
    print(f'{visited=}')
    print(f'{graph[start]=}')
    print(f'{graph[start] - visited=}')

    for next in graph[start] - visited:
        print(f'{next=}')
        dfs(graph, next, visited)
    return visited


dfs(graph, 0)

