from algorithms import search

array = [1, 5, 6, 2, 7, 0]
array.sort()
print(array)

a = search.binary_search(array, 5)
print(a)