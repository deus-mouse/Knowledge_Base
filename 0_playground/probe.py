from __future__ import annotations
from abc import ABC, abstractmethod


class ChairInterface(ABC):
    @abstractmethod
    def delivered(self):
        pass


class TableInterface(ABC):
    @abstractmethod
    def delivered(self):
        pass


class IkeaChair(ChairInterface):
    def delivered(self):
        print('IkeaChair delivered')


class IkeaTable(TableInterface):
    def delivered(self):
        print('IkeaTable delivered')


class GlobalChair(ChairInterface):
    def delivered(self):
        print('GlobalChair delivered')


class GlobalTable(TableInterface):
    def delivered(self):
        print('GlobalTable delivered')


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> ChairInterface:
        pass

    @abstractmethod
    def create_table(self) -> TableInterface:
        pass


class IkeaFactory:
    def create_chair(self) -> ChairInterface:
        return IkeaChair()

    def create_table(self) -> TableInterface:
        return IkeaTable()


class GlobalFactory:
    def create_chair(self) -> ChairInterface:
        return GlobalChair()

    def create_table(self) -> TableInterface:
        return GlobalTable()


class Client:
    def __init__(self, factory):
        self.factory = factory

    def supply(self):
        if self.factory == 'Ikea':
            self.FACTORY = IkeaFactory()
        elif self.factory == 'Global':
            self.FACTORY = GlobalFactory()

        chair = self.FACTORY.create_chair()
        table = self.FACTORY.create_table()

        chair.delivered()
        table.delivered()


def client_code(factory):
    client = Client(factory)
    client.supply()


client_code('Ikea')
client_code('Global')


