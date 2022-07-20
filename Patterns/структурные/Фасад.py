'''
Пожалуй, самый известный шаблон проектирования в Python.

Представьте, что у вас есть система со значительным количеством объектов. Каждый объект предлагает богатый набор методов API. Возможности этой системы велики, но ее интерфейс слишком сложный. Для удобства можно добавить новый объект, представляющий хорошо продуманные комбинации методов. Это и есть Фасад.

'''


class Car(object):
    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level