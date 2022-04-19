'''
https://www.youtube.com/watch?v=IG6oIbuSwCc
'''

from contextlib import contextmanager


# класс имитирующий какой-то объект который можно открыть (бд)
class Resource:
    def __int__(self):
        self.opened = False

    def open(self, *args):
        print(f'Resource was opened with {args=}')
        self.opened = True

    def close(self):
        print('Resorce was closed')
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memmory leak detected! Resource was not closed!')

    def action(self):
        print('Do something with resource')


# 1-й способ
@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource
    except:
        raise
    finally:
        if resource:
            resource.close()


# 2-й способ
class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()


if __name__ == '__main__':

    # resource = Resource()
    # resource.open(1, 2, 3)
    # resource.action()
    # тут мы НЕ закрыли соединени, упадет предупреждение

    with open_resource(1,2,3) as res1:
        res1.action()

    with ResourceWorker(1,2,3) as res2:
        res2.action()