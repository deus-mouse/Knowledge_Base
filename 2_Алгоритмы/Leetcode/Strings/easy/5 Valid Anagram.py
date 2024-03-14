# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

s = "anagram"
t = "nagaram"  # True

s = "rat"
t = "car"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1

        return s_count == t_count


res = Solution()
print(res.isAnagram(s, t))
