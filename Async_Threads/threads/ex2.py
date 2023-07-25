import threading
import time
import logging
import asyncio

async def as_sleep(i):
    await asyncio.sleep(i)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def first():
    logging.debug('first thread started ...')
    logging.debug('first waiting ...')
    asyncio.run(as_sleep(5))
    # cv.wait()
    logging.debug('!!!first consumed the resource')


def second(cv):
    logging.debug('second thread started ...')
    logging.debug('second waiting ...')
    asyncio.run(as_sleep(5))
    logging.debug('!!!second consumed the resource')

if __name__ == '__main__':
    first_th = threading.Thread(name='first', target=first)
    # second_th = threading.Thread(name='second', target=second)

    first_th.start()
    print('go next1')
    first_th.join()

    print('go next2')


