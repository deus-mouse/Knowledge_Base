# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from typing import Optional

list1 = [1,2,4]
list2 = [1,3,4]  # Output: [1,1,2,3,4,4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Присоединяем оставшийся фрагмент
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # Вернуть dummy.next как голову нового отсортированного списка, пропуская фиктивный начальный узел.
        return dummy.next


# Создание списка 1->2->3->4->5
head1 = ListNode(1, ListNode(2, ListNode(4)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
s = Solution()
reversed_head = s.mergeTwoLists(head1, head2)

# Вывод нового списка
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

