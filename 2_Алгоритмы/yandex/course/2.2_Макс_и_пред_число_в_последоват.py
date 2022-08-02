# Дана последовательность чисел длиной N (N > О)
# Найти максимальное число в последовательности.

seq = [1, 2, 3, 4, 2]
# seq = [-1, -2, -3, -4, -2]


def find(seq):
    prev, main = min(seq[0], seq[1]), max(seq[0], seq[1])
    for i in range(2, len(seq)):
        if main < seq[i]:
            prev = main
            main = seq[i]
    return print(f'1 -> {main=} / {prev=}')

find(seq)


