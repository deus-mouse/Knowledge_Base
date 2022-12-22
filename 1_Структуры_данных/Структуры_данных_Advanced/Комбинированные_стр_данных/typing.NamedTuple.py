# Поля неизменяемы:

from typing import NamedTuple

class Car(NamedTuple):
    цвет: str
    пробег: float
    автомат: bool


car1 = Car('red', 3812.4, 22)

print(car1)
print(car1.цвет)







