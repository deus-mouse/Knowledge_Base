
# Бесконечный цикл
def repeater(value):
    while True:
        yield value


for x in repeater(1):
    print(x)
    break

r = repeater(2)
print(f'{r=}')
print(f'{next(r)=}')
print(f'{r.__next__()=}')


# цикл с отсновкой БЕЗ StopIteration
def three_times_repeater(value):
    yield value
    yield value
    yield value


for i in three_times_repeater('Hi'):
    print(f'three_times_repeater={i}')


iterator = three_times_repeater('Hi2')
# for i in range(4):
#     print(f'three_times_repeater2={next(iterator)=}')


def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator2 = bounded_repeater('Hi3', 4)
for i in range(4):
    print(f'bounded_repeater={next(iterator2)=}')
