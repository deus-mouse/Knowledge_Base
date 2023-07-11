from __future__ import annotations
from abc import ABC, abstractmethod



class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProduct:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProduct:
        pass


class Factory1(AbstractFactory):
    def create_product_a(self) -> AbstractProduct:
        return ProductA1()

    def create_product_b(self) -> AbstractProduct:
        return ProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self) -> AbstractProduct:
        return ProductA2()

    def create_product_b(self) -> AbstractProduct:
        return ProductB2()


class AbstractProduct(ABC):
    @abstractmethod
    def run(self):
        pass


class ProductA1(AbstractProduct):
    def run(self):
        print('ProductA1')


class ProductA2(AbstractProduct):
    def run(self):
        print('ProductA2')


class ProductB1(AbstractProduct):
    def run(self):
        print('ProductB1')


class ProductB2(AbstractProduct):
    def run(self):
        print('ProductB2')


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.run()
    product_b.run()

client_code(Factory1())
client_code(Factory2())