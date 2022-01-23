#  Сортировка выборкой
nums = [5,7,23,7,45,8]
print('Было', nums)
for i in range(len(nums)):
    lowest = i  # первый элемент примем за наименьший
    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j  # нашли элемент меньше в правом срезе

    nums[i], nums[lowest] = nums[lowest], nums[i]

print('Стало', nums)