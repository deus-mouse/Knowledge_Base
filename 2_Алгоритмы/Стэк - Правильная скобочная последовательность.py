# по методу LIFO

hooks = '()[]{}<>'
open = hooks[::2]
closed = hooks[1::2]
print(f'{open=}')
print(f'{closed=}')

def foo(data):
    stack = list()
    for char in data:
        if char not in hooks:
            continue
        else:
            if char in open:
                stack.append(char)
            else:
                # stack должен быть пустым
                if stack and stack.pop() == hooks[hooks.index(char)-1]:
                    continue
                else:
                    return False
    return True if not stack else False

data1 = ']({[()]})'
data2 = '(2 + 5) * {[10+ 4] - (*ds)}'
data3 = '({()]})'
data4 = '({()})'
print(foo(data1))
print(foo(data2))
print(foo(data3))
print(foo(data4))
