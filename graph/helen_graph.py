# Класс для представления graphического объекта
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        # добавляет ребра в неориентированный graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Функция для присвоения цвета вершинам Graph
def colorGraph(graph, n):
    # отслеживает цвет, присвоенный каждой вершине
    result_top_to_color = {}

    # назначает цвет вершинам один за другим
    for u in range(n):

        # проверяет цвета смежных вершин `u` и сохраняет их в наборе
        # assigned = set([result.get(i) for i in graph.adjList[u] if i in result])

        #######-> Roma
        ll = []
        for i in graph.adjList[u]:
            if i in result_top_to_color:
                ll.append(result_top_to_color.get(i))
        assigned = set(ll)
        #####

        # проверка первого бесплатного цвета
        color = 1


        for c in assigned:
            if color != c:
                break
            color = color + 1

        # назначает вершине `u` первый доступный цвет
        result_top_to_color[u] = color

    q_colors = max(result_top_to_color.values())  # Roma определяем макс кол-во цветов
    result_color_to_top = {i: [] for i in range(1, q_colors + 1)}  # {1: [], 2: [], 3: []}

    for k, v in result_top_to_color.items():
        result_color_to_top[v].append(k)

    return q_colors, result_color_to_top


# Жадная раскраска Graph
if __name__ == '__main__':

    # Список ребер Graph согласно приведенной выше схеме
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

    # общее количество узлов в Graph (от 0 до 5)
    n = 6

    # строит graph по заданным ребрам
    graph = Graph(edges, n)

    # Цветной Graph # с использованием жадного алгоритма
    q_colors, result_color_to_top = colorGraph(graph, n)

    print(f'Number of colors: {q_colors}')
    print(f'Color cases is: {result_color_to_top}')
