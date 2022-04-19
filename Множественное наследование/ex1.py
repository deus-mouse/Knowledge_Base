'''
https://www.youtube.com/watch?v=4N-Q74IJd9U
'''

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


# class Styles:
#     def __init__(self, color = 'red', width = 1, *args):
#         print('class Styles')
#         self._color = color
#         self._width = width
#         print(f'{self._color=}')
#         print(f'{self._width=}')
#         super().__init__(*args)
#
#
# class Pos:
#     def __init__(self, sp : Point, ep : Point, *args):
#         print('class Pos')
#         self._sp = sp
#         self._ep = ep
#         print(f'{self._sp=}')
#         print(f'{self._ep=}')
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')



# но можно так
class Styles:
    def __init__(self):
        print('class Styles')
        # super()


class Pos:
    def __init__(self):
        print('class Pos')
        # super()


# class Line(Pos, Styles):
class Line(Styles, Pos):
    def __init__(self, sp : Point, ep : Point, color = 'red', width = 1):
        self._color = color
        self._width = width
        print(f'{self._color=}')
        print(f'{self._width=}')
        self._sp = sp
        self._ep = ep
        print(f'{self._sp=}')
        print(f'{self._ep=}')
        super()

    def draw(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


obj = Line(Point(10, 10), Point(100, 100), 'green', 5)
obj.draw()