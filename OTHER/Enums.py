from enum import Enum, unique, auto


class MyClass1(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


print(f'{MyClass1.ONE=}, {MyClass1.ONE.name=}, {MyClass1.ONE.value=}')
print(f'{MyClass1.TWO=}, {MyClass1.TWO.name=}, {MyClass1.TWO.value=}')
print(f'{MyClass1.THREE=}, {MyClass1.THREE.name=}, {MyClass1.THREE.value=}')

for item in MyClass1:
    print(f'{item=}, {item.name=}, {item.value=}')


class MyClass2(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()


for item in MyClass2:
    print(f'{item=}, {item=}, {item=}')


class PrintableEnum(Enum):
    def __str__(self):
        return self.name.lower()


class Colours(PrintableEnum):
    BLUE = "\33[94m"
    GREEN = "\33[92m"
    YELLOW = "\33[93m"


print(f'{Colours.BLUE.value}this text is {Colours.BLUE.name}')
print(f'{Colours.GREEN.value}this text is {Colours.GREEN.name}')
print(f'{Colours.YELLOW.value}this text is {Colours.YELLOW.name}')
