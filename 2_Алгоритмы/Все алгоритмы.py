# Сортировка пузырьком
nums = [1, 3, 2, 8, 4, 9, 22]
print(nums)
swaps = True
while swaps:
    swaps = False
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)


# Факториал числа
number = 5
def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 0
    while i < n:
        i += 1
        f = f * i
    return f
print(factorial(number))


# Число фибоначчи
def fib():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

for i, f in zip(range(10+1), fib()):
    print('{i:3}:{f:3}'.format(i=i, f=f))


# Расстояние Левенштейна
str1 = 'Neuronet'
str2 = 'Neurne'
def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            # Если строка пустая, то расттояние равняется ее длине (n вставок)
            return max(i, j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковые просто съедаем их
            return rec(i-1, j-1)
        else:
            # иначе считаем минимальный вариант
            return 1 + min(
                rec(i, j-1), # удаление символа
                rec(i-1, j), # вставка символа
                rec(i-1, j-1),) # замена символа
    return rec(len(a), len(b))

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100
print(lev)
print(pct)


# Односвязный список
class Node:
    # ячейка списка
    def __init__(self, value = None, next = None):
        self.value =  value
        self.next = next

class LinkedList:
    # односвязный список
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head != None:
            c = self.head
            out = 'LinkedList [' + str(c.value)

            while c.next != None:
                c = c.next
                out += ', ' + str(c.value)

            out += ']'
            return out
        else:
            return 'LinkedList []'

    def add(self, n):
        self.length += 1

        if self.head == None:
            self.head = self.tail = Node(n, None)
        else:
            self.tail.next = self.tail = Node(n, None)

    def reverse(self):
        # разворачивание односвязного списка
        pNode = None
        cNode = self.head
        nNode = cNode.next

        self.tail = cNode

        while nNode != None:
            cNode.next = pNode
            pNode = cNode
            cNode = nNode
            nNode = cNode.next

        cNode.next = pNode
        self.head = cNode

L = LinkedList()

L.add(1)
L.add(2)
L.add(3)
print(L)
L.reverse()

print(L)


# Сортировка выборкой
nums = [5,7,23,7,45,8]
print('Было', nums)
for i in range(len(nums)):
    lowest = i  # первый элемент примем за наименьший
    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j  # нашли элемент меньше в правом срезе

    nums[i], nums[lowest] = nums[lowest], nums[i]

print('Стало', nums)


# Линейный поиск
names = ['Роман', 'Лена', 'Денис', 'Тоня']
search_for = 'Тоня'
def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # вохвращаем индекс

    return None  # или None если не найдено

print(linear_search(names, search_for))


# Бинарный поиск
nums = [4, 4, 6, 2, 56, 32, 67, 99]
nums.sort()  # сортируем
print(nums)

search_for = 67  # что ищем

lowest = 0
highest = len(nums) - 1
index = None  # будущий индекс искомого элемента

while (lowest <= highest) or (index is None):
    # повторяем пока не найдено
    mid = (lowest + highest) // 2  # середина

    if nums[mid] == search_for:
        # нашли посередине
        index = mid
        break
    else:
        if search_for < nums[mid]:
            # Ищем в левой части списка
            highest = mid - 1
            print('highest', highest)
        else:
            # Ищем правой части списка
            lowest = mid + 1
            print('lowest', lowest)
    print('index', index)

print('Искомый элемент ', search_for, 'находится под индексом ', index)


# Алгоритм Евклида НОД
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

print("НОД чисел 30, 18 = ", gcd(30, 18))

# ИЛИ
import math

i = math.gcd(30, 18)
print(i)


# Переворот строки
some_string = 'Neuronet Neuronet'

def reverse_string(s):
    chars = list(s)  # разбираем строку на символы

    for i in range(len(s) // 2):
        # до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)

print(some_string)
print(reverse_string(some_string))


# Самый быстрый и легкий способ в Python
print(some_string[::-1])
