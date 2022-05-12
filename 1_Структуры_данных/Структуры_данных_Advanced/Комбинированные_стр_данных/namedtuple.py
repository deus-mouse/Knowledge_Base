from collections import namedtuple

user = namedtuple('User', 'name age gender')

data = ['Roman', 45, 'male']

user1 = user(name='Roman', age=45, gender='male')
print(f'{user1=}')
print(f'{type(user1)=}')

print(f'{user1[0]=}')
print(f'{user1.gender=}')