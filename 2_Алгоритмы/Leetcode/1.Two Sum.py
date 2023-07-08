nums = [3,2,4]
target = 6


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1 in range(len(nums)):
            print(f'{i1=}')
            for i2 in range(i1+1, len(nums)):
                print(f'{i2=}')
                if nums[i1] + nums[i2] == target:
                    return [i1, i2]
        return None


# solution = Solution()
# print(solution.twoSum(nums, target))


class Solution2(object):
    def twoSum(self, nums, target):
        table = {}

        for i in range(len(nums)):
            if nums[i] not in table:  # если там есть такое число, с необходимой разницей, то нашли
                table[(target-nums[i])] = i  # заносится разница между порядковым числом и результатом
                print(f'{i=}')
                print(f'{table=}')
            else:
                return [i, table[nums[i]]]


solution2 = Solution2()
print(solution2.twoSum(nums, target))
