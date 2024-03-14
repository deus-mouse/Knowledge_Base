# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
from typing import Optional

head = [1,2,3,4,5]
n = 2


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # использование фиктивного (dummy) узла в начале списка.
        # Это обеспечивает удобную обработку краевых случаев,
        # когда требуется удалить головной узел списка,
        # а также позволяет избежать дополнительных проверок на None для head списка.
        dummy.next = head
        fast = slow = dummy

        # Передвигаем fast вперед на n + 1 позиций, чтобы между slow и fast было n узлов
        for _ in range(n + 1):
            fast = fast.next

        # Двигаем slow и fast вместе, пока fast не достигнет конца списка
        while fast:
            slow = slow.next
            fast = fast.next

        # Удаляем n-й узел с конца
        slow.next = slow.next.next

        return dummy.next


# Создание списка 1->2->3->4->5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
s = Solution()
new_head = s.removeNthFromEnd(head, n)

# Вывод нового списка
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Выведет: 1 -> 2 -> 3 -> 5 -> None

