for'''
E. Анаграммы

Даны две строки, состоящие из строчных латинских букв. 
Требуется определить, являются ли эти строки анаграммами, 
т. е. отличаются ли они только порядком следования символов.
'''

import sys
from collections import defaultdict

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

def str_to_dict(s):
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    return d

def anogrammer(a, b):
    return 1 if str_to_dict(a) == str_to_dict(b) else 0

print(anogrammer(a, b))




n = int(input("input n: "))
s = str(n)
l = len(s)
for i in range(l//2):
    if s[i] != s[-1-i]:
       print("It's not palindrome")
       break
else:
    print("It's palindrome")