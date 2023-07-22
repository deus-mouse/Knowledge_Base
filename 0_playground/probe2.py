from datetime import time


def calculator(*args):
    total = 1
    for number in args:
        total *= number ** 9000
    return len(str(total))


def time_track_2(func):
    def surrogate(*args):
        started_at = time()
        result = func(*args)
        ended_at = time()
        elapsed = round(ended_at - started_at, 2)
        print(f'Elapsed 3 = {elapsed}')
        return result
    return surrogate


calculator = time_track_2(calculator)
result = calculator(2134, 7322, 9586, 8584)
print(result)
