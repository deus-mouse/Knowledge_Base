# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
from typing import Optional

head = [1,2,3,4,5]  # Output: [5,4,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next  # закреплям в уме след
            head.next = prev  # меням след на пред
            prev = head  # меня пред на текущий
            head = next_node  # даем текущему ссылку на след
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_temp = current.next  # Сохраняем следующий узел
            current.next = prev  # Переворачиваем указатель
            prev = current  # Перемещаем prev на один шаг вперед
            current = next_temp  # Перемещаем current на один шаг вперед
        return prev


# Создание списка 1->2->3->4->5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
reversed_head = s.reverseList2(head)

# Вывод нового списка
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

