class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        from numpy import median
        l = 0
        r = 1
        med = median(nums)
        n = len(nums)
        while l < n and r < n:
            while l < n and nums[l] <= med:
                l += 2
            while r < n and nums[r] >= med:
                r += 2
            if l < n and r < n:
                nums[l], nums[r] = nums[l], nums[r]


sol = Solution()
sol.wiggleSort([1,3,2,2,3,1])