


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


foo = counter()
print(foo())  # 1
print(foo())  # 2
print(foo())  # 3