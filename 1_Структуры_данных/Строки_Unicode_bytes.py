'''
https://pyneng.readthedocs.io/ru/latest/book/16_unicode/python_3_unicode.html
'''

r = r"dsfdf"  # неизменяемая строка


print("\N{LATIN SMALL LETTER O WITH DIAERESIS}")  # название символа "ö"
print("\u00F6")  # или utf-код символа "ö"


# Unicode
print("\u043f\u0440\u0438\u0432\u0435\u0442")  # "привет"
print(f"{ord('п')=}")  # 1087
print(f"{chr(1087)=}")  # "п"


# Bytes
b1 = b'\xd0\xb4\xd0\xb0'
b2 = b"\xd0\xb4\xd0\xb0"
b3 = b'''\xd0\xb4\xd0\xb0'''
print(f'{b1=}')  # b1=b'\xd0\xb4\xd0\xb0'
print(f'{b2=}')  # b2=b'\xd0\xb4\xd0\xb0'
print(f'{b3=}')  # b3=b'\xd0\xb4\xd0\xb0'

bytes1 = b'hello'
print(f'{bytes1.hex()=}')  # '68656c6c6f'