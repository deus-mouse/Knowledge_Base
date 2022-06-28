from math import sqrt

# print(sqrt(9))


def squarty(func):
    def wrapper():
        return sqrt(func())
    return wrapper


@squarty
def digit():
    return 9



def not_null_ar_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"получили {args=}, {kwargs=}")
        return func(*args, **kwargs)
    return wrapper


@not_null_ar_decorator
def my_foo(first, second):
    return f"{first=}, {second=}"


print(f"{my_foo('Roman', 'Helen')}")