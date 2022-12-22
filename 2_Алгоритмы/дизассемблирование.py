import dis


# создание кортежа tuple
print(dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval')))

# создание списка list
print(dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval')))