
def foo(s):
    if not s:
        return ''
    result = ''
    block = []

    for char in s:
        # print(f'{char=}')
        if char not in result:
            result += char
            # print(f'{result=}')
        else:
            block.append(result)
            # print(f'{block=}')
            result = char
    block.append(result)

    # print(f'{block=}')
    return max(block, key=len)


print(foo('abcabcbb'))
print(foo('abcbb'))
print(foo('bbbbb'))
print(foo('pwwkew'))
print(foo('pwwke'))
print(foo(''))
print(foo('pww kew'))
print(foo('pww kew54467'))


