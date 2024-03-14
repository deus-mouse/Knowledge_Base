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
        if not head or not head.next:
            return True

        slow, fast = head, head
        # Находим середину списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Переворачиваем вторую половину списка
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Сравниваем две половины
        left, right = head, prev
        while right:  # Достаточно сравнить только вторую половину
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



