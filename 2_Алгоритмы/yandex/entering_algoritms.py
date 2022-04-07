from collections import defaultdict

'''
Дана бинарная последовательность. Сколько подряд "1"?
f([1, 1, 0, 0, 0, 1, 1, 1]) = 3
'''

def foo1(data):
    current, best = 0, 0
    for item in data:
        if item == 1:
            current += 1
            # if current > max:
            #     max = current
            best = max(current, best)
        else:
            current = 0
    return best

# print(foo1([1, 1, 0, 1, 1, 1]))
# print(foo1([1, 1, 1, 0, 1, 1]))


'''
Даны 2 строки
Являетлся ли они анограммами (отличаются лишь порядклм следования букв)
'''
#1
def foo2(str1, str2):
    print(f'{sorted(list(str1))=}')
    print(f'{sorted(list(str2))=}')
    return sorted(list(str1)) == sorted(list(str2))

# print(foo2('romann', 'ramonn'))

#2
def stringtodict(s):
    s_dict = defaultdict(int)
    print(f'{s_dict=}')
    for char in s:
        s_dict[char] += 1
    print(f'{s_dict=}')
    return s_dict

def foo3(s1, s2):
    return stringtodict(s1) == stringtodict(s2)

# print(foo3('romann', 'ramonn'))
# print(foo3('', ''))


'''
Генерирование правильной скобочной последовательности
'''
# https://clck.ru/ejJJ9 схема

def generate(cur, open, closed, n):
    print(f'{open=}')
    print(f'{closed=}')

    print(f'---- {cur=}')
    if len(cur) == n*2:
        print('len(cur) == n*2')
        if open == closed:
            print(f'!!!! {cur=}')
        # return

    if open < n:
        print('generate 1')
        generate(cur + '(', open + 1, closed, n)
    if closed < open:
        print('generate 2')
        generate(cur + ')', open, closed + 1, n)

def foo4(n):
    generate('', 0, 0, n)

foo4(3)
