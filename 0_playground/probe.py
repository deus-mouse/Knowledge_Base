# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head
        # где середина?
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # переворот второй половины
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            print(f'{left.val=}, {right.val=}')
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# Создание списка 1->2->3->4->5
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
s = Solution()
new_head = s.isPalindrome(head)
print(new_head)



