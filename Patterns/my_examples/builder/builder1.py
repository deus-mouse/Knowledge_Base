from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    def __init__(self):
        self._product = None

    def reset(self):
        self._product = Product()

    @property
    @abstractmethod
    def product(self):
        product = self._product
        self.reset()
        return product

    def buildStepA(self):
        pass

    def buildStepB(self):
        pass

    def buildStepC(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def buildStepA(self):
        self._product.add('part1')

    def buildStepB(self):
        self._product.add('part2')

    def buildStepC(self):
        self._product.add('part3')


class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f'{self.parts=}')


class Director:
    def __init__(self):
        self._builder: Builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_min(self):
        self.builder.buildStepA()

    def build_max(self):
        self.builder.buildStepA()
        self.builder.buildStepB()
        self.builder.buildStepC()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    director.build_min()
    director.builder.product.list_parts()

    director.build_max()
    director.builder.product.list_parts()

