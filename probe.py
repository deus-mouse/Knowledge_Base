
seq = [1, 2, 3, 4, 2]

def find_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans

print(f'{find_x(seq, 2)=}')

def find_x2(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return ans

print(f'{find_x2(seq, 2)=}')


def find_x3(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

print(f'{find_x3(seq, 2)=}')


def find_x4(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[-i] == x:
            return len(seq)-i
    return ans

print(f'{find_x4(seq, 2)=}')


