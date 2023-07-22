from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction(ABC):
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        print(f'Base: {self.implementation.implementation_operation()=}')


class ExtendedAbstraction(Abstraction):
    def operation(self):
        print(f'Extended: {self.implementation.implementation_operation()=}')


class Implementation(ABC):
    @abstractmethod
    def implementation_operation(self):
        pass


class ConcreteImplementationA(Implementation):
    def implementation_operation(self):
        print(f'ConcreteImplementationA')


class ConcreteImplementationB(Implementation):
    def implementation_operation(self):
        print(f'ConcreteImplementationB')


def client_code(abstraction: Abstraction):
    abstraction.operation()


if __name__ == '__main__':

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print('===============')

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)



