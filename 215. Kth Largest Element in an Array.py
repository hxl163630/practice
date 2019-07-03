class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        return self.quick_select(nums, 0, n - 1, n - k)

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[end]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start <= k <= right:
            return self.quick_select(nums, start, right, k)
        if left <= k <= end:
            return self.quick_select(nums, left, end, k)

        return nums[k]

sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],  2))