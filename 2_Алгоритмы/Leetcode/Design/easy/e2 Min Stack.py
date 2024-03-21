# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''

class MinStack_GPT:

    def __init__(self):
        self.stack = []  # Основной стек для хранения элементов
        self.minStack = []  # Вспомогательный стек для хранения минимальных элементов

    def push(self, val):
        self.stack.append(val)  # Добавляем элемент в основной стек
        # Если вспомогательный стек пуст или новый элемент меньше текущего минимума,
        # добавляем его в вспомогательный стек
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        val = self.stack.pop()  # Удаляем элемент с вершины основного стека
        # Если удаленный элемент совпадает с вершиной вспомогательного стека,
        # также удаляем его оттуда
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]  # Возвращаем верхний элемент основного стека

    def getMin(self):
        return self.minStack[-1]  # Возвращаем минимальный элемент из вспомогательного стека

'''
Big O анализ эффективности:
Временная сложность: Все методы (push, pop, top, getMin) работают за постоянное время 
O(1), так как добавление, удаление и доступ к элементу в конце списка (или стека) выполняются за 
O(1), а вспомогательный стек позволяет мгновенно получать минимальный элемент.
Пространственная сложность: 
O(n) в худшем случае, где n — количество элементов в стеке. Это происходит, когда все элементы стека убывают, и каждый элемент дублируется в minStack.
'''


# Your MinStack object will be instantiated and called as such:
obj = MinStack_GPT()
obj.push(val=5)
obj.push(val=2)
obj.push(val=10)
print(f'{obj.stack=}')

# obj.pop()
param_3 = obj.top()
print(f'{param_3=}')
param_4 = obj.getMin()
print(f'{param_4=}')


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # return sorted(self.stack)[0]
        return min(*self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val=5)
# obj.push(val=2)
# obj.push(val=10)
# print(f'{obj.stack=}')
#
# # obj.pop()
# param_3 = obj.top()
# print(f'{param_3=}')
# param_4 = obj.getMin()
# print(f'{param_4=}')


