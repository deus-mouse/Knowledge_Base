from collections import defaultdict

food_list = 'ham ham ham bread'

# food_count = defaultdict(lambda : 0)
food_count = defaultdict(int)
print(f'{food_count=}')

for food in food_list.split(" "):
    food_count[food] += 1

print(f'{food_count=}')
print(f'{dict(food_count)=}')


def greet(name):
    return 'hi ' + name

greeter = defaultdict(lambda: greet)
print(f'{greeter["default"]("Roman")=}')
print(f'{greeter=}')