from datetime import datetime, timedelta
import asyncio
from threading import Thread


def async_foo():
    time1 = datetime.now()
    while True:
        time2 = datetime.now() - timedelta(seconds=5)
        if time1 < time2:
            print(f'{time2=}')
            return




def foo():
    th = Thread(target=async_foo)
    th.start()
    print('foo')


foo()

