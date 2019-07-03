class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        l = 0
        r = len(nums) - 1
        output = 0
        while l < r:
            if nums[l] + nums[r] == target:
                while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                    l += 1
                while r >= 0 and nums[r] == nums[r - 1]:
                    r -= 1
                output += 1
                if l >= r: break
                l += 1
                r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return output


sol = Solution()
sol.twoSum6([7, 11, 11, 1, 2, 3, 4], 22)
