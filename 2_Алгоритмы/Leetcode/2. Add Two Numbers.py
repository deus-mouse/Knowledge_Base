
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# WORKED
class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


# MY not Worked
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1_str = str(l1)
        # l2_str = str(l2)
        l1_str = ''
        l2_str = ''
        while l1 and l2:
        # for _ in range(len(l1)):
            l1_str = ''.join([l1_str, str(l1.val)])
            l1 = l1.next
            l2_str = ''.join([l2_str, str(l2.val)])
            l2 = l2.next

        # l1_str = ''.join(str(x) for x in l1_str[::-1] if x.isdigit())
        # l2_str = ''.join(str(x) for x in l2_str[::-1] if x.isdigit())

        result_int = int(l1_str[::-1]) + int(l2_str[::-1])
        result_str = str(result_int)
        result_list = [int(x) for x in result_str]
        return result_list[::-1]


l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()
print(f'{solution.addTwoNumbers(l1, l2)=}')

# print(str(l1))


