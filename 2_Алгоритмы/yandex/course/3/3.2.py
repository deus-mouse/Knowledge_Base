# Дан словарь из N слов, длина каждого не превосходит К
# В записи каждого из М слов текста (каждое длиной до К)
# может быть пропущена одна буква. Для каждого слова
# сказать, входит ли оно (возможно, с одной пропущенной
# буквой), в словарь

import random
import string

# letters = string.ascii_lowercase
# dictionary = [''.join(random.choice(letters) for i in range(10)) for _ in range(20)]
# print(dictionary)
dictionary = ['rgnhvlpgmg', 'ssvplollnv', 'fnpyckhqia', 'ghdrmyaxqq', 'rdwphnqljx', 'lqfiywhatd', 'tkypyjvtpo',
              'rznhzewudb', 'fgbmzqlnpe', 'ygytvzjluc', 'bluefqlkbi', 'cggdmzcnzn', 'lbyjhqavtt', 'vooffvqlhp',
              'yacmifdoqe', 'icyenxinuj', 'bcwamwkxqa', 'fddgkzsviq', 'cyanlyovph', 'kktpghfodq']
text = ['rgnhlpgmg', 'ssvplonv', 'fnpyckia', 'ghdrxqq', 'rdwpnqljx', 'lqfiywatd', 'tkypvtpo', ]

 
# Решение за O(Nk^2 + М)
# Выбросим из каждого слова словаря по одной букве всеми
# возможными способами за O(Nk) и положим получившиеся
# слова в множества
# Для каждого слова из текста просто проверим, есть ли оно
# в словаре за 0(1)
def foo1(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
    ans = []
    for word in text:
        ans.append(word) if word in goodwords else None
    return ans


print(f'{foo1(dictionary, text)=}')
