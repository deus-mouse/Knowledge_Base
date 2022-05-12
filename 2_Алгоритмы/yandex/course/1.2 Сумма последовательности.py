
# вводим набор чисел через пробел.
# дробим и преобразовываем в лист
seq = list(map(int, input().split()))
print(f'{seq=}')

# 1
def foo1(seq):
    if len(seq) == 0:
        return 0
    else:
        seqsum = seq[0]
        for i in range(1, len(seq)):
            seqsum += seq[i]
        return seqsum


print(f'{foo1(seq)=}')


# 2 без лишнего условия на проверку ввода
def foo2(seq):
    seqsum = 0
    for i in range(len(seq)):
        seqsum += seq[i]
    return seqsum


print(f'{foo2(seq)=}')
