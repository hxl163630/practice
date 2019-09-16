class Solution:
    def kConcatenationMaxSum(self, arr, k):
        def getMaxArray(nums):
            n = len(nums)
            curr_sum = max_sum = nums[0]

            for i in range(1, n):
                curr_sum = max(nums[i], curr_sum + nums[i])
                max_sum = max(max_sum, curr_sum)

            return max(0, max_sum)

        total = sum(arr)
        if k == 1:
            return getMaxArray(arr)
        if total <= 0:
            return getMaxArray(arr + arr)

        return getMaxArray(arr + [total * (k - 2)] + arr)

sol = Solution()
print(sol.kConcatenationMaxSum([1,-2,1], 5))
