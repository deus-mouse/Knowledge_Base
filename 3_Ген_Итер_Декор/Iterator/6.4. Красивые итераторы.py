
# Бесконечный итератор
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


repeater = Repeater('Hi')
for item in repeater:
    print(f'{item=}')
    break
####################################################

iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(f'{item=}')
    break

####################################################
iterator = iter(repeater)
print(f'{next(iterator)=}')

####################################################
#Более емко

class Repeater2:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value


repeater_2 = Repeater2('Hi2')
for item_2 in repeater_2:
    print(f'{item_2=}')
    break

####################################################
# класс, который прекращает итерации после заданного количества повторений:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter >= self.max_repeats:
            raise StopIteration
        self.counter += 1
        return self.value


repeater_3 = BoundedRepeater('Hi', 3)
iterator = iter(repeater_3)
while True:
    try:
        item_3 = next(iterator)
    except StopIteration:
        break
    print(f'{item_3=}')

