'''
5
'''
import random

# array = []
# for _ in range(50):
#     array.append(random.randint(0, 1000))
# print(f'{array=}')

array = [389, 580, 401, 493, 389, 912, 470, 417, 4, 20, 842, 544, 868, 803, 438, 473, 848, 929, 402, 327, 117, 591, 106,
         639, 611, 610, 526, 573, 245, 407, 535, 812, 113, 722, 603, 139, 565, 198, 244, 591, 204, 134, 380, 751, 429,
         409, 81, 772, 379, 932]

def my_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less_then = []
    more_then = []
    for elem in array:
        if elem > pivot:
            more_then.append(elem)
        elif elem < pivot:
            less_then.append(elem)
    return my_sort(less_then) + [pivot, ] + my_sort(more_then)


def cleaner(array):
    # sort_array = sorted(array)
    sort_array = my_sort(array)
    print(f'{sort_array=}')
    del sort_array[:int(len(array)/10)]
    del sort_array[-int(len(array)/10):]
    return sort_array

print(f'{cleaner(array)=}')
print(f'{len(cleaner(array))=}')



