import asyncio
from time import sleep
debug = 1


async def main():
    print('main')
    task = asyncio.create_task(foo('foo'))
    if not debug:
        print('not debug')

        # sleep(2)
        # print(f'{task.result()=}')
        return
    await task
    print(f'{task.result()=}')
    print(f'main finished')




# async def foo(text):
def foo(text):
    print(text)
    # await asyncio.sleep(1)
    return 100


asyncio.run(main())

