# Быстрая сортировка начинается с разбиения списка — выбора одного значения списка, которое будет в его отсортированном
# месте. Это значение называется опорным. Все элементы, меньшие, чем этот элемент, перемещаются влево. Все более крупные
# элементы перемещены вправо.
# Зная, что опорный элемент находится на своем правильном месте, мы рекурсивно сортируем значения вокруг этого
# элемента, пока не будет отсортирован весь список.

# Сортировка же пузырьком выполняет итерации по списку, сравнивая элементы попарно и меняя их местами,
# пока более крупные элементы не перестанут «всплывать» до конца списка, а более мелкие элементы не будут
# оставаться «снизу».

# Реализация Quick Sort
def partition(nums, low, high):
    # Выбираем средний элемент, в качестве опорного. Некоторые реализации выбирают
    # первый элемент или последний элемент или вообще случайный элемент.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент в i (слева от оси) больше, чем
        # элемент в J (справа от оси), то поменять их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создаем вспомогательную рекурсивную функцию
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после опорного элемента, по которому наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Проверяем, что все работает
random_list_of_nums = [4, 22, 5, 1, 1, 18, 18, 150, 99]
quick_sort(random_list_of_nums)
# print(random_list_of_nums)


################################################################

# быстрая сортировка
def my_sort_v2(slist):
    if len(slist) <= 1:
        return slist
    pivot = slist[0]
    less_then = []
    more_then = []
    for elem in slist:
        if elem > pivot:
            more_then.append(elem)
        elif elem < pivot:
            less_then.append(elem)
    return my_sort(less_then) + [pivot, ] + my_sort(more_then)


################################################################

# быстрая сортировка с lambda
def quick_sort_with_lambda(s):
    if len(s) <= 1:
        return s
    pivot = s[0]
    left_list = list(filter(lambda x: x < pivot, s))
    center = [i for i in s if i == pivot]
    right_list = list(filter(lambda x: x > pivot, s))
    # print(left_list)
    # print(center)
    # print(right_list)

    return quick_sort_with_lambda(left_list) + center + quick_sort_with_lambda(right_list)



# встроенная сортировка
def my_sort(slist):
    return list(set(sorted(slist)))


print(quick_sort_with_lambda(random_list_of_nums))