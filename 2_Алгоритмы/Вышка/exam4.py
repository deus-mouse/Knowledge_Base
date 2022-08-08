'''
4
'''
import random

# array = []
# for _ in range(50):
#     array.append(random.randint(0, 1000))
# print(f'{array=}')

array = [[389, 580, 401, 493],[389, 912, 470, 417, 4], [20, 842, 544], [868, 803, 438, 473, 848, 929], [402], [327, 117], [591, 106,
         639, 611, 610, 526, 573], [245, 407, 535], [812, 113], [722, 603, 139], [565, 198, 244, 591, 204], [134, 380, 751], [429],
         [409, 81, 772, 379, 932]]


# def get_pairs(array):
#     list_of_pairs = []
#     for index in range(len(array)):
#         if index == 0:
#             continue
#         pairs_elements = [array[index-1], array[index]]
#         list_of_pairs.append(pairs_elements)
#     return list_of_pairs
#

def maximum_sum(list_of_pairs):
    maxi = 0
    #обходим внешний список
    # for l in list_of_pairs:
    #     maxi = max(sum(l), maxi)
    # return maxi

    cur = 0
    for index in range(len(list_of_pairs)):
        if index == 0:
            continue
        elif max(sum(list_of_pairs[index]), maxi) > maxi:
            maxi = max(sum(list_of_pairs[index]), maxi)
            print(f'{maxi=}')
            cur = index
    return cur


def foo(array, m):

    goods = 0
    ind = 0
    for i in range(len(array)):
        if goods < sum(array[i]):
            goods = sum(array[i])
            ind = i

    tmp = array
    for j in range(m):

        l = random.randint(0, len(array)-1)  # кроме ind
        m = random.randint(0, len(array[l])-1)  # кроме ind
        k = random.randint(0, len(array[ind])-1)  # кроме ind
        tmp[ind][k] = array.pop([l][m])
        tmp[ind][k] = array.pop([l][m])

        if goods > sum(array(tmp[ind])):
            s_array = []
            for i in range(0, len(tmp)-1):
                if s_array[0] < sum(array(tmp[i])):
                    s_array=[sum(array(tmp)), i]

        if s_array < goods:
            goods = s_array[0]

        array = tmp

    return goods

        # list_of_pairs = get_pairs(array)
        # print(f'{list_of_pairs=}')
        # index_max = maximum_sum(list_of_pairs)
        # print(f'{index_max=}')
        # random_for_first_element = random.randint(0, len(list_of_pairs[index_max])-1)
        #
        # print(f'!!! {list_of_pairs[index_max]=}')
        #
        # first_element = list_of_pairs[index_max].pop(random_for_first_element)
        # print(f'{first_element=}')
        #
        # random_for_second_index_element = random.randint(0, len(list_of_pairs)-1)
        # random_for_second_element = random.randint(0, len(list_of_pairs[index_max])-1)
        #
        # print(f'!!! {list_of_pairs[random_for_second_index_element]=}')
        #
        #
        # second_element = list_of_pairs[random_for_second_index_element].pop(random_for_second_element)
        # print(f'{second_element=}')
        #
        # list_of_pairs[index_max].append(second_element)
        # list_of_pairs[random_for_second_index_element].append(first_element)
        #
        # print(f'!!! {list_of_pairs[index_max]=}')
        # print(f'!!! {list_of_pairs[random_for_second_index_element]=}')


foo(array, 10)




