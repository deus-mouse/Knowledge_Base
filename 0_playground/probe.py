


class SingletonMeta(type):

    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(f'{id(s1) == id(s2) = }')