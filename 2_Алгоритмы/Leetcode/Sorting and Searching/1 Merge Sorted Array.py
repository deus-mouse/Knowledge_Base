# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Установите указатель i на последний элемент nums1 (принимая во внимание только элементы до m),
        # указатель j на последний элемент nums2,
        # и указатель k на последнее место в массиве nums1 (включая дополнительное место для элементов nums2).
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Копируем оставшиеся элементы из nums2, если они есть
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Примеры использования
s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
s.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Выведет: [1,2,2,3,5,6]

nums1 = [1]
s.merge(nums1, 1, [], 0)
print(nums1)  # Выведет: [1]

nums1 = [0]
s.merge(nums1, 0, [1], 1)
print(nums1)  # Выведет: [1]