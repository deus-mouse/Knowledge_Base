# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
from typing import List

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

class Solution:

    def intersect_gpt(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Creating a dictionary to keep track of elements and their counts in nums1
        # делаем defaultdict из nums1
        count_nums1 = {}
        for num in nums1:
            if num in count_nums1:
                count_nums1[num] += 1
            else:
                count_nums1[num] = 1

        # Creating the intersection list
        intersection = []
        for num in nums2:
            # смотрим есть ли число из nums2 в nums1 и проверяем что его счетчик к defaultdict еще не скручен
            if num in count_nums1 and count_nums1[num] > 0:
                intersection.append(num)
                count_nums1[num] -= 1  # скручиваем счетчик в defaultdict чтобы получить мин макс кол-во возможных вхождений

        return intersection

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return nums1 & nums2  # только для множеств
        result = []
        similar = set(nums1) & set(nums2)
        for i in similar:
            r = min(nums1.count(i), nums2.count(i))
            result.extend([i] * r)
        return result




s = Solution()
print(s.intersect(nums1, nums2))
print(s.intersect_gpt(nums1, nums2))