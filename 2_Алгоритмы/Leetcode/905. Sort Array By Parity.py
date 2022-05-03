nums = [3,1,2,4]
# chars = ['b', '43', 'd', 'c']


# my solution
class Solution(object):
    def sortArrayByParity(self, nums=None, chars=None):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                nums.insert(0, nums.pop(index))

        return nums


s = Solution()
print(s.sortArrayByParity(nums))


# them solution
class Solution2(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort(key=lambda x: x % 2)
        return nums


s2 = Solution2()
print(s2.sortArrayByParity(nums))




