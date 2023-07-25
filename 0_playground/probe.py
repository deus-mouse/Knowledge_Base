import inspect
import threading

nlu_results = []


def logger(data):
    '''usage: logger(f'{MSISDN=}')'''
    func = inspect.stack()[1][3]
    if func == '<module>':
        func = ''
    print(f'+++ {func}: {data}')


def main_nlu(r):
    if r:
        payload = {
            'input': r,
            'regex': r,
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

        except Exception as e:
            logger('reserve_recognition, error message: ', e)

        nlu_results.append(payload)
        # return func(r if (r.has_intents() or r.has_entities() or not r_nlu) else r_nlu)
        return r_nlu


def nlu(func):
    '''decorator for additional recognition by regex + nlu'''

    def surrogate(r):  # r <- regex
        nlu_thread = threading.Thread(name='nlu_thread', target=main_nlu, args=(r,))
        nlu_thread.start()
        if r and r == 'R':
            return func(r)
        else:
            nlu_thread.join()
            return func(nlu_thread.value)

    return surrogate


@nlu
def logic(r):
    logger(f'{r=}')


logic(r='R')
logic(r='NLU')
