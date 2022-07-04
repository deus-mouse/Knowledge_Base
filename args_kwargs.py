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