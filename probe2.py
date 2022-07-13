

def foo():
    print(f'{foo.__name__=}')


def main():
    print(f'{main.__name__=}')
    print(f'2 -> {__name__=}')


if __name__ == '__main__':
    main()
