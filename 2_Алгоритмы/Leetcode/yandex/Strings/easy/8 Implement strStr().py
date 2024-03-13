# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

import re


class Solution:
    def strStr_GPT(self, haystack: str, needle: str) -> int:
        # Special cases
        if not needle:
            return 0
        if not haystack:
            return -1

        # Length of the needle
        needle_len = len(needle)

        # Iterate through the haystack
        for i in range(len(haystack) - needle_len + 1):
            # Check if the substring matches the needle
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

    def strStr_REGEX(self, haystack: str, needle: str) -> int:
        pos = -1
        match = re.search(needle, haystack)
        if match:

            pos = match.span()[0]
        return pos


res = Solution()
# print('1:', res.strStr('sadbutsad', 'sad'))  # 3
# print('1:', res.strStr('leetcode', 'leeto'))  # -1
print('1:', res.strStr_REGEX('hello', 'll'))  # 2
