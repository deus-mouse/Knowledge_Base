# #обычная функция
#
# def fibo_func(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
# fibo = fibo_func(100)
# for value in fibo:
#     print(value)
#
#
# #ITERATOR
#
# class Fibo_iter:
#     def __init__(self, n):
#         self.a, self.b, self.i, self.n = 0, 1, 0, n
#
#     def __iter__(self):
#         self.a, self.b, self.i = 0, 1, 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration
#             self.a, self.b = self.b, self.a + self.b
#         return self.a
#
# fibo_iter = Fibo_iter(100)
# for value in fibo_iter:
#     print(value)
#
# ####################################################
# class Solar_system():
#     def __init__(self):
#         self.i = 0
#         self.one = 'Mercury'
#         self.two = 'Venus'
#         self.three = 'Earth'
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i == 1:
#             return f'I am - {self.one}'
#         if self.i == 2:
#             return f'I am - {self.two}'
#         if self.i == 3:
#             return f'I am - {self.three}'
#         if self.i == 4:
#             return f'I am - {__class__.__name__}'
#         raise StopIteration
#
# iter = Solar_system()
# for value in iter:
#     print(value)
#
# print(f'{iter=}')
# print(f'{type(iter)=}')


class My_List():
    def __init__(self, seq):
        self.seq = seq
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration
        result = self.seq[self.index]
        self.index += 1
        return result


my_list = My_List([1, 2, 3])

for item in my_list:
    print(f'{item=}')