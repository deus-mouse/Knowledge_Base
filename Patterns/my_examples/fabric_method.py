from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractUniversity(ABC):
    def some_method(self):
        pass

    @abstractmethod
    def create(self):
        pass


class ScienceUniversity(AbstractUniversity):
    def create(self) -> StudentInterface:
        return Scientist()


class HeroUniversity(AbstractUniversity):
    def create(self) -> StudentInterface:
        return Hero()


class MilitaryUniversity(AbstractUniversity):
    def create(self) -> StudentInterface:
        return Soldier()


class StudentInterface(ABC):
    @abstractmethod
    def save_world(self):
        pass


class Scientist(StudentInterface):
    def save_world(self):
        print('Sciencist saved the world')


class Hero(StudentInterface):
    def save_world(self):
        print('Hero saved the world')


class Soldier(StudentInterface):
    def save_world(self):
        print('Soldier saved the world')


def client_code(university: AbstractUniversity):
    unit = university.create()
    unit.save_world()


unit_1 = client_code(ScienceUniversity())
unit_2 = client_code(HeroUniversity())
unit_3 = client_code(MilitaryUniversity())