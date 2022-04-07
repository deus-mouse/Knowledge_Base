# Бинарный поиск
'''
Бинарное дерево представляет собой структуру,
в которой каждый узел (или вершина) имеет не более двух узлов-потомков и в точности одного родителя.
Самый верхний узел дерева является единственным узлом без родителей; он называется корневым узлом.
'''

nums = [4, 4, 6, 2, 56, 32, 67, 99]
nums.sort()  # сортируем
print(nums)

search_for = 67  # что ищем

lowest = 0
highest = len(nums) - 1
index = None  # будущий индекс искомого элемента

while (lowest <= highest) or (index is None):
    # повторяем пока не найдено
    mid = (lowest + highest) // 2  # середина

    if nums[mid] == search_for: 
        # нашли посередине
        index = mid
        break
    else:
        if search_for < nums[mid]:
            # Ищем в левой части списка
            highest = mid - 1
            print('highest', highest)
        else:
            # Ищем правой части списка
            lowest = mid + 1
            print('lowest', lowest)
    print('index', index)

print('Искомый элемент ', search_for, 'находится под индексом ', index)
