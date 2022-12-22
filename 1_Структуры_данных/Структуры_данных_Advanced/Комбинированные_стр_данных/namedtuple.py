from collections import namedtuple

user = namedtuple('User', 'name age gender')

data = ['Roman', 45, 'male']

user1 = user(name='Roman', age=45, gender='male')
print(f'{user1=}')
print(f'{type(user1)=}')

print(f'{user1[0]=}')
print(f'{user1.gender=}')



p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)

print(p1.y)