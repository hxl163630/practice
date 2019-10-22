from typing import List
def find_two_swapped(nums: List[int]) -> (int, int):
    n = len(nums)
    x = y = -1
    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            y = nums[i + 1]
            # first swap occurence
            if x == -1:
                x = nums[i]
            # second swap occurence
            else:
                break
    return x, y

print(find_two_swapped([5,2,3,4,1,0]))