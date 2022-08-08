# Игра PitCraft происходит в двумерном мире, который состоит
# из блоков размером 1 на 1 метр. Остров игрока представляет
# собой набор столбцов различной высоты, состоящих из блоков
# камня и окруженный морем. Над островом прошёл сильный
# дождь, который заполнил водой все низины, а не поместившаяся
# в них вода стекла в море, не увеличив его уровень
# По ландшафту острова определите, сколько блоков воды осталось
# после дождя в низинах на острове.


island = [3, 1, 4, 3, 5, 1, 1, 3, 1]
island = [3, 1, 12, 3, 5, 1, 1, 20, 1]

# мое решение
def my_island_filler(island):
    waters = 0
    top_index = 0
    for vertex_index in range(0, len(island)):
        if island[vertex_index] > island[top_index]:
            top_index = vertex_index

    # наполняем слева направо до вершины
    index_max = 0
    for index in range(1, top_index):
        if island[index_max] <= island[index]:
            index_max = index
            continue
        elif island[index_max] > island[index]:
            points = island[index_max] - island[index]
            island[index] += points
            waters += points

    # наполняем справа налево до вершины
    index_max = len(island) - 1
    for index in reversed(range(top_index, len(island))):
        if island[index_max] <= island[index]:
            index_max = index
            continue
        elif island[index_max] > island[index]:
            points = island[index_max] - island[index]
            island[index] += points
            waters += points

    print(f'{island=}')
    print(f'{waters=}')


my_island_filler(island)