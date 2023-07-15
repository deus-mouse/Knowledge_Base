
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_str = str(l1)
        l2_str = str(l2)
        l1_str = ''.join(str(x) for x in l1_str[::-1] if x.isdigit())
        l2_str = ''.join(str(x) for x in l2_str[::-1] if x.isdigit())
        result_int = int(l1_str) + int(l2_str)
        result_str = str(result_int)
        result_list = [int(x) for x in result_str]
        return result_list[::-1]


l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()
print(f'{solution.addTwoNumbers(l1, l2)=}')

# print(str(l1))
