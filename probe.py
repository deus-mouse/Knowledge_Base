class Fibo_iter:
    def __init__(self, n):
        self.a, self.b, self.i, self.n = 0, 1, 0, n

    def __iter__(self):
        self.a, self.b, self.i = 0, 1, 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
        return self.a

fibo_iter = Fibo_iter(100)
for value in fibo_iter:
    print(value)