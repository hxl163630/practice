def insertionSort(nums, size):
    for i in range(1, size):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums = [6, 5, 3, 2, 8, 10, 9]
size = len(nums)
insertionSort(nums, size)