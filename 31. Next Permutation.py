class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1: return
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]: i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums = nums[::-1]


sol = Solution()
sol.nextPermutation([1,3,2])
