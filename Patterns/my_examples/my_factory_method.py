from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractUniversity(ABC):
    def some_method(self):
        pass

    @abstractmethod
    def create(self):
        pass


class ScienceUniversity(AbstractUniversity):
    def create(self) -> UnitInterface:
        return Scientist()


class HeroUniversity(AbstractUniversity):
    def create(self) -> UnitInterface:
        return Hero()


class MilitaryUniversity(AbstractUniversity):
    def create(self) -> UnitInterface:
        return Soldier()


class UnitInterface(ABC):
    @abstractmethod
    def save_world(self):
        pass


class Scientist(UnitInterface):
    def save_world(self):
        print('Sciencist saved the world')


class Hero(UnitInterface):
    def save_world(self):
        print('Hero saved the world')


class Soldier(UnitInterface):
    def save_world(self):
        print('Soldier saved the world')


def client_code(university: AbstractUniversity):
    unit = university.create()
    unit.save_world()


unit_1 = client_code(ScienceUniversity())
unit_2 = client_code(HeroUniversity())
unit_3 = client_code(MilitaryUniversity())