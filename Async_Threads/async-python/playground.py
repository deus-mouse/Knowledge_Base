import asyncio

import os
import time
# To work with the .env file
# from dotenv import load_dotenv
# load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []

start = time.time()


async def get_symbols():
    result = None
    time.sleep(2)
    result = 'RESULT'
    print(f'{result=}')
    return result

# result = asyncio.run(get_symbols())  #  тоже самое что и 3 строчки ниже, только в одну
loop = asyncio.get_event_loop()
loop.run_until_complete(get_symbols())
loop.close()
# end = time.time()
# total_time = end - start
# print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
# print('You did it!')

print(f'=============')

# new_result = ' '.join([result, '!!!!'])
# print(f'{new_result=}')
