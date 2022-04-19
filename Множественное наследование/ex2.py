'''
https://www.youtube.com/watch?v=MBbVq_FIYDA
'''


# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used


class Figure:
    def __init__(self, figure=None):
        self.figure = figure


class Rectangle(Figure):
    def __init__(self, length, width, figure):
        self.length = length
        self.width = width
        print('class Rectangle')
        super().__init__(figure)

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width, figure='square')

    def area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width, figure='cube')
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
print(f'{square.figure=}')
print(f'{cube.figure=}')
