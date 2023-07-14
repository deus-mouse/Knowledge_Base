from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> ProductInterface:
        pass

    @abstractmethod
    def create_product_b(self) -> ProductInterface:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ProductInterface:
        return ConcreteProductA1()

    def create_product_b(self) -> ProductInterface:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ProductInterface:
        return ConcreteProductA2()

    def create_product_b(self) -> ProductInterface:
        return ConcreteProductB2()


class ProductInterface(ABC):
    @abstractmethod
    def run(self):
        pass


class ConcreteProductA1(ProductInterface):
    def run(self):
        print(f'run {self.__class__.__name__}')


class ConcreteProductB1(ProductInterface):
    def run(self):
        print(f'run {self.__class__.__name__}')


class ConcreteProductA2(ProductInterface):
    def run(self):
        print(f'run {self.__class__.__name__}')


class ConcreteProductB2(ProductInterface):
    def run(self):
        print(f'run {self.__class__.__name__}')


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_a.run()
    product_b = factory.create_product_b()
    product_b.run()


client_code(ConcreteFactory1())
client_code(ConcreteFactory2())
