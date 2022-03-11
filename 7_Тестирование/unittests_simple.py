import unittest


def my_sort(slist):
    '''
    >>> my_sort([3, 2, 1])
    [1, 2, 3]
    '''
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist


my_sort([3, 2, 1])

try:
    assert my_sort([3, 2, 1]) == [1, 2, 3]  # simple
except Exception as ex:
    print(ex)
else:
    print('assert ok')


class MySortTest(unittest.TestCase):
    def test_normal(self):
        result = my_sort([3, 2, 1])
        self.assertEqual(result, [1, 2, 3])

    def test_negative(self):
        result = my_sort([-3, 2, 1])
        self.assertEqual(result, [-3, 1, 2])

    def test_failed(self):
        result = my_sort([-3, 2, 1])
        self.assertEqual(result, [-3, 1, 6])


if __name__ == '__main__':
    unittest.main()
