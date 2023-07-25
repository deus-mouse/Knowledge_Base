import threading
import time
import logging
import asyncio

async def as_sleep(i):
    await asyncio.sleep(i)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def consumer(cv):
    print(f'{cv=}')
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        # asyncio.run(as_sleep(5))
        cv.wait()
        logging.debug('!!!Consumer consumed the resource')


def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        asyncio.run(as_sleep(5))
        logging.debug('Notifying to all consumers')
        cv.notify_all()


if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    # cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    # pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    # cs2.start()
    # time.sleep(5)
    # pd.start()


