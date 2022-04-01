# 1
def foo(nums):
    current = 0
    best = 0
    for n in nums:
        if n > 0:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best

mass = [1, 1, 0, 1, 1, 1, 0]
print(foo(mass))


###############################################################################
# 2
from collections import defaultdict

s1 = 'aabc'
s2 = 'cbaa'

def string_to_dict(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    print(f'{d=}')
    return d

def anagramm_checker(s1, s2):
    # return s1 == s2[::-1]  # палиндром
    return string_to_dict(s1) == string_to_dict(s2)

print(anagramm_checker(s1, s2))


###############################################################################
# 3

def generate(cur, open, closed, n):
    if len(cur) == 2 * n:
        print(cur)
        return
    if open < n:
        generate(cur + '(', open + 1, closed, n)
    if closed < open:
        generate(cur + ')', open, closed + 1, n)

def parens(n):
    generate('', 0, 0, n)

print(parens(3))
