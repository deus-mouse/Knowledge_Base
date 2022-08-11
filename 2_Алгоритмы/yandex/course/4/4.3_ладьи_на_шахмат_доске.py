# На шахматной доске N х N находятся М ладей (ладья бьет
# клетки на той же горизонтали или вертикали до ближайшей занятой)
# Определите, сколько пар ладей бьют друг друга.
# Ладьи задаются парой чисел I и J, обозначающих координаты клетки.
# 1 < N < 10^9, 0 <= M <= 2*10^5

# Решение
# Для каждой занятой горизонтали и вертикали будем хранить
# количество ладей на них. Количество пар в горизонтали
# (вертикали) равно количество ладей минус 1. Суммируем
# это количество пар для всех горизонталей и вертикалей


def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)