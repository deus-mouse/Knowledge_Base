bri = set(['Бразилия', 'Россия', 'Индия'])

print(bri)


class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


car1 = Car('красный', 3812.4, True)
car2 = Car('синий', 40231.0, False)

car2.windshield = 'треснутое'


print(car2.windshield)