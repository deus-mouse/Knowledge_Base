from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())



'''pattern Builder'''


class Builder(ABC):
    @property  # getter
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        print('!')
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add('Part1')

    def produce_part_b(self):
        self._product.add('Part2')

    def produce_part_c(self):
        self._product.add('Part3')


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> list:
        print(f'{self.parts=}')
        return self.parts


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_valuable_product(self) -> None:
        self.builder.produce_part_a()

    def build_complete_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder  # setter

    print(f'{getframeinfo(currentframe()).lineno=}')
    director.build_minimal_valuable_product()
    print(f'{getframeinfo(currentframe()).lineno=}')
    builder.product.list_parts()

    print(f'{getframeinfo(currentframe()).lineno=}')
    director.build_complete_product()
    print(f'{getframeinfo(currentframe()).lineno=}')
    builder.product.list_parts()


    print(f'{getframeinfo(currentframe()).lineno=}')
    builder.produce_part_b()
    print(f'{getframeinfo(currentframe()).lineno=}')
    builder.produce_part_a()
    print(f'{getframeinfo(currentframe()).lineno=}')
    builder.product.list_parts()
