# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        lengths = [len(s) for s in strs]
        smallest = min(lengths)
        for i in range(smallest):
            chars = [s[i] for s in strs]
            if len(set(chars)) == 1:
                res = ''.join([res, chars[0]])
                continue
            else:
                break
        return res

    def longestCommonPrefix_GPT(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as a potential prefix
        prefix = strs[0]

        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Gradually shorten the prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                print(f'{prefix=}')
                if not prefix:
                    return ""

        return prefix


res = Solution()
print('1:', res.longestCommonPrefix_GPT(["flower","flow","flight"]))  # fl
# print('1:', res.longestCommonPrefix(["dog","racecar","car"]))  # ''
