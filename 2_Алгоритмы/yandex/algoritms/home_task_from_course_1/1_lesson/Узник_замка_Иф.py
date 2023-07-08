"""
Занятие 1. Узник замка Иф
За многие годы заточения узник замка Иф проделал в стене
прямоугольное отверстие размером D х Е. Замок Иф сложен из кирпичей,
размером А х В х С. Определите, сможет ли узник выбрасывать кирпичи в
море через это отверстие, если стороны кирпича должны быть
параллельны сторонам отверстия.
"""


def bubble_sort(data):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaps = True
    return data


def foo(hole, brick):
    d, e = bubble_sort(hole)
    a, b, c = bubble_sort(brick)
    if d >= a and e >= b:
        return True
    return False


print(f'{foo([5, 5], [2, 10, 3])=}')
print(f'{foo([5, 2], [2, 10, 5])=}')
print(f'{foo([10, 5], [11, 10, 30])=}')

