'''
Напишите алгоритм поиска двух элементов в массиве натуральных чисел, произведение которых
максимально. Определите вычислительную сложность вашего алгоритма.
'''

data = [1, 3, 5, 7, 2, 1, 5, 9, 6, 1]
data = []
data = [1, 2, 5, 7, 2, 1, 5, -9, 6, 1]

best = 0
for index in range(len(data)):
    if not data:
        break
    elif not isinstance(data[index], int):
        break
    elif index == 0:
        continue
    current = data[index-1] * data[index]
    if current > best:
        best = current

print(best)


data = [1, 2]

data2 = data

data2[0] = data[1]
data2[0] = data[1]


print(data2)