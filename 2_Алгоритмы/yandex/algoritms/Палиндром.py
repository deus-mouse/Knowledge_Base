palindrom1 = 'А роза упала, на лапу Азора'


def is_polindrom(phrase):
    index_start = 0
    index_last = len(phrase)-1
    flag = True
    while index_start < index_last:
        while not phrase[index_start].isalpha():
            index_start += 1
        while not phrase[index_last].isalpha():
            index_last -= 1

        if phrase[index_start].lower() != phrase[index_last].lower():
            flag = False
            break
        else:
            index_start += 1
            index_last -= 1

    return flag

print(f'{is_polindrom(palindrom1)=}')