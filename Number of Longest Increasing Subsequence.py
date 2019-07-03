class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 1] for _ in nums]
        dp[0] = [1, 1]
        res = 0
        for i, num in enumerate(nums):
            if i == 0: continue
            j = i - 1
            while num < nums[j] and j >= 0:

                j -= 1
                dp[i][1] = dp[j][1] + 1
            dp[i][0] = dp[j][0] + 1
        maxl = max(dp ,key=lambda e: int(e[0]))
        for l in dp:
            if l[0] == maxl: res += 1
        return res


sol = Solution()
sol.findNumberOfLIS([1,3,5,4,7])