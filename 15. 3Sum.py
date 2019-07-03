class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # THIS WORKS BECAUSE WE CAN SOLVE A 2SUM PROBLEM WITH A SORTED ARRAY BY USING
        # 2 POINTERS. ONE FROM THE LEFT AND ONE FROM THE RIGHT.

        if len(nums) < 3:
            return []

        nums = sorted(nums)
        res = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            summ = 0 - nums[i]

            while left < right:

                if (nums[left] + nums[right] == summ):
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif (nums[left] + nums[right] < summ):
                    left += 1
                else:
                    right -= 1
        return res

sol = Solution()
#print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([1,0,0,0]))
