import pytest

# seq = list(map(int, input().split()))
# seqmax = 0
#
# # 1
# for i in range(len(seq)):
#     if seq[i] > seqmax:
#         seqmax = seq[i]
#
# print(seqmax)


# 2
def max_sequence(seq):
    if len(seq) == 0:
        seqmax = '-inf'
    else:
        seqmax = seq[0]
        for i in range(1, len(seq)):
            if seq[i] > seqmax:
                seqmax = seq[i]
    return seqmax


# 3
# print(max(seq))


@pytest.mark.parametrize('seq, expected_result',
                         [('5 6 7 8 55 9 3 22', 55),
                          ('4 5 6 7 3 33 6 77', 77),
                          ('4 5 101 7 3 33 6 77', 101),
                          ('444 5 101 7 3 33 6 77', 444),
                          ('444 5 101 7 3 33 6 555', 555),
                          ('5 5 5 5 5 5 5 5', 5),
                          ('5', 5),
                          ('', '-inf'),
                          ('-2 -4 -6', -2),
                          ])
def test_max_sequence(seq, expected_result):
    seq = list(map(int, seq.split()))
    assert max_sequence(seq) == expected_result