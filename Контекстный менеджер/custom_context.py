import time
from contextlib import contextmanager

def calculator(*args):
    total = 1
    for number in args:
        print(f'{number=}')

        total *= number ** 9000
    print(f'{len(str(total))=}')
    return len(str(total))


# как класс
class TimeTrack:
    def __init__(self, *args):
        self.started_at = time.time()
        print(f'{self.started_at=}')
        self.payload = args
        print(f'{self.payload=}')

    def __enter__(self):
        self.result = calculator(*self.payload)
        print(f'{self.result=}')
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ended_at = time.time()
        print(f'{self.ended_at=}')
        self.elapsed = round(self.ended_at - self.started_at, 4)
        print(f'Elapsed 2 = {self.elapsed}')


with TimeTrack(2134, 7322, 9586, 8584) as my_time_track:
    print('КЛАСС: тут выполняется то, что обернуто')


# как функция
@contextmanager
def time_track(*args):
    try:
        started_at = time.time()
        yield calculator(*args)
    finally:
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Elapsed 2 = {elapsed}')


with time_track(2134, 7322, 9586, 8584) as my_time_track:
    print('ФУНКЦИЯ: тут выполняется то, что обернуто')
