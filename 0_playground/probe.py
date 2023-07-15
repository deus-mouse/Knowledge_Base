from abc import ABC, abstractmethod


class Builder(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add('Part1')

    def produce_part_b(self):
        self._product.add('Part2')

    def produce_part_c(self):
        self._product.add('Part3')


class Director:
    def __init__(self):
        self._builder: Builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def produce_mvp_product(self):
        self._builder.produce_part_a()

    def produce_complete_product(self):
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()


class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f'{self.parts=}')


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    director.produce_mvp_product()
    builder.product.list_parts()

    director.produce_complete_product()
    builder.product.list_parts()


