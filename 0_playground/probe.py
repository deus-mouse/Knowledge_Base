import inspect


class Target:
    def request(self):
        return f'{inspect.stack()[0][3]=}'


class Adaptee:
    def specific_request(self):
        return f'{inspect.stack()[0][3]=}'


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f'{inspect.stack()[0][3]=} | {self.adaptee.specific_request()=}'


def client_code(target: Target):
    print(f'{target.request()=}')


if __name__ == '__main__':
    target = Target()
    print(f'{target.request()=}')

    adaptee = Adaptee()
    print(f'{adaptee.specific_request()=}')

    adapter = Adapter(adaptee)
    print(f'{adapter.request()=}')
