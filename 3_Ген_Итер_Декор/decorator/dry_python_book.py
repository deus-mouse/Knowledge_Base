
# ДЕКОРАТОРЫ


def null_decorator(func):
    return func


def foo1():
    return 'my foo for null_decorator'


print(f'{null_decorator(foo1())=}')


@null_decorator
def foo2():
    return 'my foo2 for null_decorator'


print(f'{foo2()=}')


#################


def uppercase(func):
    def wrapper():
        # original = func()
        # modified = original.upper()
        # return modified
        return func().upper()
    return wrapper


@uppercase
def foo3():
    return 'my foo3 for null_decorator'


print(f'{foo3()=}')


# ВЛОЖЕННЫЕ ДЕКОРАТОРЫ
# выполянется снизу вверх


def add_strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def add_emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@add_strong
@add_emphasis
def foo4():
    return 'multiple decorators for foo4'


print(f'{foo4()=}')


# ДЕКОРАТОРЫ С ПРОБРОСОМ АРГУМЕНТОВ


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: called {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() return {original_result!r}')

        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(f"{say('Lena', 'Im hungry')}")


# ОТЛАЖИВАЕМЫЕ ДЕКОРАТОРЫ

import functools

def uppercase_debug(func):
    @functools.wraps(func)
    # без / c встроенного декоратора будет вывод
    # greet.__doc__
    # >>>           / """ВЕРНУТЬ..."""
    # greet.__name__
    # >>> 'wrapper'  /  'greet'
    def wrapper():
        return func().upper()
    return wrapper


@uppercase_debug
def greet():
    """ВЕРНУТЬ ДРУЖЕСКОЕ ПРИВЕТСТВИЕ"""
    return 'Hello!'

