# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Создание списка 1->2->3->4->5
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n2  # cycle here

s = Solution()
new_head = s.hasCycle(n1)
print(new_head)
# new_head = s.hasCycle(head2)
# print(new_head)



