# имя сохраняется оригинальное "some_foo"
# без @wraps было бы "inner"

from functools import wraps


def decorator(func):
    @wraps(func)
    def inner(value):
        value = value ** 2
        func(value)
    return inner


@decorator
def some_foo(value):
    print(f'{value}')


some_foo(4)
print(f'{some_foo.__name__=}')

