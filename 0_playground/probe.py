from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class Factory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def run_a(self):
        pass


class ProductA1(AbstractProductA):
    def run_a(self):
        print(f'run ProductA1')


class ProductA2(AbstractProductA):
    def run_a(self):
        print(f'run ProductA2')


class AbstractProductB(ABC):
    @abstractmethod
    def run_b(self):
        pass


class ProductB1(AbstractProductB):
    def run_b(self):
        print(f'RUN ProductB1')


class ProductB2(AbstractProductB):
    def run_b(self):
        print(f'RUN ProductB2')


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.run_a()
    product_b.run_b()


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(Factory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(Factory2())