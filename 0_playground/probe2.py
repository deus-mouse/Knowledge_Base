import inspect
from threading import Thread
from time import sleep

nlu_results = []


def logger(data):
    '''usage: logger(f'{MSISDN=}')'''
    func = inspect.stack()[1][3]
    if func == '<module>':
        func = ''
    print(f'+++ {func}: {data}')


class CustomThread(Thread):
    # constructor
    def __init__(self, r):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.value = None
        self.nlu_results = []
        self.r = r

    def run(self):
        if self.r:
            payload = {
                'input': self.r,
                'regex': self.r,
                'nlu': {},
            }

            logger('nlu response:')
            r_nlu = None
            try:
                # 1st option how we can realize reserve nlu recognition
                r_nlu = 'r_nlu'  # <- nlu

                # 2nd option
                # r.set_nlu_ver('3.0')
                # r_nlu = nlu.extract(r.utterance())

                if r_nlu:
                    intents = ['r_nlu._intents']

                    # removing patterns from r_nlu result
                    if intents:
                        payload.update({'nlu': intents})
                sleep(5)

            except Exception as e:
                logger('reserve_recognition, error message: ', e)

            self.nlu_results.append(payload)
            # return func(r if (r.has_intents() or r.has_entities() or not r_nlu) else r_nlu)
            self.value = r_nlu
            # return r_nlu


def nlu(func):
    '''decorator for additional recognition by regex + nlu'''

    def surrogate(r):  # r <- regex
        nlu_thread = CustomThread(r)
        nlu_thread.start()
        if r and r == 'R':
            print(f'{nlu_thread.nlu_results=}')
            return func(r)
        else:
            nlu_thread.join()
            print(f'{nlu_thread.nlu_results=}')
            return func(nlu_thread.value)
    return surrogate



@nlu
def logic(r):
    logger(f'{r=}')


logic(r='R')
print('========================')
logic(r='NLU')


# # create a new thread
# thread = CustomThread()
# # start the thread
# thread.start()
# # wait for the thread to finish
# thread.join()
# # get the value returned from the thread
# data = thread.value
# print(data)
