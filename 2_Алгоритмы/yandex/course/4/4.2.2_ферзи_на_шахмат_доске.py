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


data = [[3, 1], [1, 3], [3, 3], [5, 2], [3, 5], [5, 3]]
data2 = [[1, 1], [2, 4], [3, 1], [3, 3], [4, 2], [5, 3]]


def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def addrook_slash(back_or_forward, key):
        if key not in back_or_forward:
            back_or_forward[key] = 0
        back_or_forward[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    rooks_in_b_slash = {}
    rooks_in_f_slash = {}

    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)

        addrook_slash(rooks_in_b_slash, key=col-row)
        addrook_slash(rooks_in_f_slash, key=col+row)
    # print(f'{rooksinrow=}')
    # print(f'{rooksincol=}')
    # print(f'{rooks_in_b_slash=}')
    # print(f'{rooks_in_f_slash=}')
    result = countpairs(rooksinrow) + countpairs(rooksincol) + countpairs(rooks_in_b_slash) + countpairs(rooks_in_f_slash)

    return result

print(f'{countbeatingrooks(data2)=}')