

s = '1 1 4 2 3 0 2 3'
input = [2, -4]
# coards = [[x, y] for x, y in s.split(' ', 2)]
new_s = s.replace(' ', '')
# coards = [[y, x] for x, y in [new_s.pop(), new_s.pop()]]
# # print([new_s.pop(), new_s.pop()])
#
# print(new_s)
# # print(coards)
# #
#
# coards = []
#
# print(coards)
#
#
# print(77 % 11)
# print(54 // 11)

class ABC:
    some = 'some'
    __some_private = '_some_private'

    def a(self):
        some = 'a_some'
        print('a')

    @classmethod
    def b(cls):
        cls.some = 'b_some'
        print('b')

    @staticmethod
    def c():
        some = 'c_some'
        print('c')

# print(ABC.a())
ABC.b()
ABC.c()
# print(ABC.__some_private)
cl = ABC()
cl.a()
print(cl.some)
cl.b()
print(cl.some)
cl.c()

print(cl.some)
print(cl._ABC__some_private)

