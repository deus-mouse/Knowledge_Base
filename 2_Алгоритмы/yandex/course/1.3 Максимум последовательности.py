
seq = list(map(int, input().split()))


# 1
# если все введенные числа будут отрицательны, то мы выведем ноль, т.к. ноль больше любого отрицательного числа
def max_sequence1(seq):
    seqmax = 0
    for i in range(len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
    return seqmax


print(f'{max_sequence1(seq)=}')


# 2
def max_sequence2(seq):
    if len(seq) == 0:  # обработаем пустой ввод
        seqmax = '-inf'
    else:
        seqmax = seq[0]  # вместе с этим если он НЕ пустой, то seqmax переопределится внутри цикла и выведет верное значение
        for i in range(1, len(seq)):
            if seq[i] > seqmax:
                seqmax = seq[i]
    return seqmax


print(f'{max_sequence2(seq)=}')


# 3 MY
def max_sequence_my(seq):
    return max(seq)


print(f'{max_sequence_my(seq)=}')


import pytest

@pytest.mark.parametrize('seq, expected_result',
                         [('5 6 7 8 55 9 3 22', 55),  # посередине
                          ('4 5 6 7 3 33 6 77', 77),  # в конце
                          ('4 5 101 7 3 33 6 77', 101),  # в начале
                          ('444 5 101 7 3 33 6 77', 444),
                          ('444 5 101 7 3 33 6 555', 555),
                          ('5 5 5 5 5 5 5 5', 5),  # все одинаковые
                          ('5', 5),  # всего один
                          ('', '-inf'),  # пустой ввод
                          ('-2 -4 -6', -2),  # отрицательный
                          ])
def test_max_sequence(seq, expected_result):
    seq = list(map(int, seq.split()))
    assert max_sequence2(seq) == expected_result