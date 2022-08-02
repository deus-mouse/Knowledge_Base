# Дана последовательность чисел длиной N (N > О)
# Найти максимальное число в последовательности.

seq = [1, 2, 3, 4, 2]
# seq = [-1, -2, -3, -4, -2]


def max_element(seq):
    max = seq[0]
    for i in range(1, len(seq)):
        if max < seq[i]:
            max = seq[i]
            # здесь объект дублируется, переприсваивается
            # это плохо для других языков, где построение не на ссылках как в питоне
    return print(f'1 -> {max=}')

max_element(seq)


# решение - теперь мы будем опираться на индекс
def max_element2(seq):
    ind = 0
    for i in range(1, len(seq)):
        if seq[ind] < seq[i]:
            ind = i
    return print(f'2 -> {seq[ind]=}')

max_element2(seq)

