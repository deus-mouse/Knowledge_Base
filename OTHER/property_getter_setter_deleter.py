

class MyClass:
    def __init__(self):
        self.__variable = None

    @property  # getter
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        self.__variable = value

    @variable.deleter
    def variable(self):
        self.__variable = None


my_class = MyClass()
print(f'{my_class.variable=}')  # None

my_class.variable = 123
print(f'{my_class.variable=}')  # 123

del my_class.variable
print(f'{my_class.variable=}')  # None
