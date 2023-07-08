'''
Занятие 2. Симметричная последовательность
Последовательность чисел назовем симметричной, если она одинаково
читается как слева направо, так и справа налево. Например, следующие
последовательности являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
Вашей программе будет дана последовательность чисел. Требуется
определить, какое минимальное количество и каких чисел надо приписать
в конец этой последовательности, чтобы она стала симметричной.
Длина последовательности до 100
'''

seq_1 = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]  # строка Грэя  True

seq_2 = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2]  # не хватает 1 в конце
seq_3 = [1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2]  # не хватает 1 в начале

# префикс функцию надо написать самому
def prefix_foo(seq):
    i = 0
    j = len(seq) - 1
    prefix = list()
    for index in range(len(seq)-1):
        count = 0
        if index == 0:
            prefix.append(count)
            continue

        if seq[index] == seq[i]:
            count += 1

            for index_2 in range(index+1, len(seq)-1):
                i += 1
                if seq[index_2] == seq[i]:
                    count += 1
                else:
                    prefix.append(count)
                    count = 0
                    i = 0
                    continue
        else:
            prefix.append(count)
            count = 0
            i = 0
        print(f'{index=}')
    return prefix


def foo(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        # перебираем сравнивая с концов к центру
        # когда пересечемся выходим
        while i < len(seq) and j >= 0 and seq[i] == seq[j] and i <= j:
            i += 1
            j -= 1

        # если левая рамка слева, а правая справа, значит палиндром найден
        if i > j:
            new_seq = []
            # разворачиваем результат чтобы потом сравнить с изначальным вводом
            for i in reversed(range(start, len(seq))):
                new_seq.append(seq[i])

            need_to_append = []
            # если не равны, то определяем что еще нужно добаваить
            if new_seq != seq:
                for i in range(len(seq)-len(new_seq)):
                    need_to_append.append(seq[i])

            return new_seq, need_to_append

# n = int(input())
# seq = list(map(int, input().split()))
ans = foo(seq_1)
print(f'{len(ans)=}')
print(*ans)

ans2 = foo(seq_2)
print(f'{len(ans2)=}')
print(*ans2)

ans3 = foo(seq_3)
print(f'{len(ans3)=}')
print(*ans3)


ans4 = prefix_foo(seq_1)
print(f'{len(ans4)=}')
print(*ans4)
