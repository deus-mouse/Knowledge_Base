
S = 'лилилось лилилась'
s = 'лилила'
s_2 = 'лииллиил'

# мое решение
def prefix_func(s):
    j = 0
    x = 0
    p = [0] * len(s)

    for i in range(1, len(s)):
        if s[i] != s[j]:
            x = 0
            # p[i] = x
            j = 0
            if s[i] == s[j]:
                x += 1
                p[i] = x
                j += 1
        else:
            x += 1
            p[i] = x
            j += 1

    return p

print(prefix_func(s))
print(prefix_func(s_2))


# решение https://www.youtube.com/watch?v=S2I0covkyMc&t=493s
def prefix_func_2(s):
    j = 0
    i = 1
    p = [0] * len(s)
    while i < len(s):
        if s[i] == s[j]:
            p[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]
    return p

print(prefix_func_2(s))
print(prefix_func_2(s_2))


# мое решение
def my_find_string(S, s):
    p = prefix_func(s)
    j = 0
    i = 0

    while i < len(s):
        if s[i] == S[j]:
            j += 1
            i += 1
        else:
            i = p[i-1]
            if s[i] != S[j]:
                j += 1
        if j == len(S)-1:
            break

    if i == len(s):
        return j
    else:
        return False


print(f'{my_find_string(S, s)=}')


# решение https://www.youtube.com/watch?v=S2I0covkyMc&t=493s
def my_find_string_2(S, s):
    p = prefix_func(s)
    m = len(s)
    n = len(S)

    i = 0
    j = 0
    while i < n:
        if S[i] == s[j]:
            i += 1
            j += 1
            if j == m:
                print('Find!')
                break

        else:
            if j > 0:
                j = p[j-1]
            else:
                i += 1

    if i == n:
        return False
    elif j == m:
        return i


print(f'{my_find_string_2(S, s)=}')
