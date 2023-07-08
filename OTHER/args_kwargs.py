
# from dry_python_book 3.4

def fo():
    print(f'{fo.__name__=}')


def foo(required, *args, **kwargs):
    print(f'{required=}')
    if args:
        print(f'{args=}')
    if kwargs:
        print(f'{kwargs=}')


fo()
# fo('arg1')

# foo()
foo('req')
foo('req', 1,2,3)
foo('req', a=1, b=2, c=3)
foo('req', 'test', a=1, b=2, c=3,)
foo('req', 'test', ['1', True, None, ...], a=1, b=2, c=3,)

#############################################################################

# from dry_python_book 3.5

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(*tuple_vec)
print_vector(*list_vec)
# <1, 0, 1>
#
# Этот прием работает для любого итерируемого объекта, включая выраже-
# ния-генераторы. В результате использования оператора * с генератором
# все поступающие из генератора элементы будут использованы и переданы
# в функцию:

genexpr = (x * x for x in range(3))
print_vector(*genexpr)
# <0, 1, 4>


# Помимо оператора * для распаковки последовательностей, в частности
# кортежей, списков и генераторов, в позиционные аргументы, также име-
# ется оператор ** для распаковки именованных аргументов, поступающих
# из словарей. Предположим, что наш вектор был представлен в виде сле-
# дующего объекта dict:

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
# <1, 0, 1>
