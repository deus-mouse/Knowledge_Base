# Сортировка пузырьком
nums = [1, 3, 2, 8, 4, 9, 22]
print(nums)
swaps = True
while swaps:
    swaps = False
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
