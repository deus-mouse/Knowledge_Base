
data = [4, 6, 8, 12, 1, 4, 2]

def countsort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval + 1)
    count = [0] * k
    print(f'{count=}')
    for now in seq:
        count[now - minval] += 1
        print(f'{count=}')
    nowpos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
    print(f'{seq=}')


countsort(data)


