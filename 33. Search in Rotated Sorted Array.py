class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if target >= nums[l]:
                if nums[m] > nums[l] and nums[m] < target: l = m
                else: r = m
            else:
                if nums[m] < nums[r] and nums[m] > target: r = m
                else: l = m
        if nums[l] == target: return l
        if nums[r] == target: return r


        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))