import random

nums = [2,7,9,3,1]

print(nums[::2])


print(random.randint(1, 100))


a = 100 ** 0.5
print(a)


d = 1000
print(d // 1100)

lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for i in reversed(lib.items()):
    print(f'{i=}')