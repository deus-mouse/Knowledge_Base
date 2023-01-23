
def integers():
    for i in range(1, 9):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
print(f'{list(chain)=}')


# ИЛИ

integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(f'{list(negated)=}')

