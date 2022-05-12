nums = [2,6,4,8,10,9,15]
# nums = [1,2,3,4]
# nums = [1]


# my solution
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while True:
            if not len(nums):
                break

            if nums[0] == min(nums):
                nums.pop(0)

            elif nums[len(nums)-1] == max(nums):
                nums.pop(len(nums)-1)

            else:
                break

        return len(nums)


s = Solution()
print(s.findUnsortedSubarray(nums))


# them solution
class Solution2:
    def findUnsortedSubarray(self, nums):
        if len(nums) < 2:
            return 0

        start, end = -1, 0
        left_prev, right_prev = nums[0], nums[start]

        for i in range(1, len(nums)):
            # find the largest index not in place
            if nums[i] < left_prev:
                end = i
            else:
                left_prev = nums[i]

            # find the smallest index not in place
            if right_prev < nums[~i]:
                start = ~i
            else:
                right_prev = nums[~i]

        if end != 0:
            return end - (len(nums) + start) + 1
        else:
            return 0


s2 = Solution2()
print(s2.findUnsortedSubarray(nums))

